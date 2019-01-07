import requests
from lxml import etree


class WanYi(object):
    def __init__(self):
        self.url = 'https://news.163.com/'
        self.headers = {
            'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        self.html_content = ''

    def get_html(self, url):
        response = requests.get(url=url, headers=self.headers)
        if not response.status_code == 200:
            raise Exception(f"请求失败, {response.status_code}")
        self.html_content = response.text

    def parse(self):
        # 解析
        tree = etree.HTML(self.html_content)

        # 每条新闻的头部要闻
        head1 = '//div[@class="mt35 mod_hot_rank clearfix"]/ul/li/a/text()'
        country = tree.xpath(head1)
        for i in country: print(i)

    def run(self):
        self.get_html(self.url)
        self.parse()


if __name__ =='__main__':
    content = WanYi()
    content.run()

