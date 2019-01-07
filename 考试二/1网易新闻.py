import requests
from lxml import etree
from fake_useragent import UserAgent

url = 'https://news.163.com/'
headers = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
if not response.status_code == 200:
    raise Exception(f"请求失败, {response.status_code}")
html_content = response.text

# 解析
tree = etree.HTML(html_content)

# 每条新闻的头部要闻
head1 = '//div[@class="mt35 mod_hot_rank clearfix"]/ul/li/a/text()'
country = tree.xpath(head1)
for i in country: print(i)