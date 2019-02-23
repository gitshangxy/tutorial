# 关键点
# 1. 首页展示的数据是通过网页源代码返回的数据，后面下拉加载的时候通过json接口返回的数据。问题:json接口如何得知网页源代码的最后一条数据？
# 2. 上一次json接口返回的数据和下一次json接口返回的数据是如何关联的？

import requests, json, re

class CSDNSpider(object):
    def __init__(self):
        self.start_url = 'https://www.csdn.net/nav/career'
        self.json_api = 'https://www.csdn.net/api/articles?type=more&category=home&shown_offset=1550738079210987'
        self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'}

    def get_list(self):
        response = requests.get(url=self.start_url, headers=self.headers)
        if response.status_code == 200:
            shown_offset = re.search(re.compile(r'<ul.*?id="feedlist_id" shown-offset="(.*?)">', re.S), response.text).group(1)
            datas = re.findall(re.compile(r'<div class="title">.*?<a.*?>(.*?)</a>.*?<div class="summary oneline">(.*?)</div>.*?<dd class="name">.*?<a.*?>(.*?)</a>.*?<dd class="time">(.*?)</dd>.*?<a .*?>(.*?)</a>.*?<a .*?>(.*?)</a>', re.S), response.text)
            for data in datas:
                char = re.compile(r'\n|\t|\r')
                title = re.sub(char, '', data[0])
                info = re.sub(char, '', data[1])
                author = re.sub(char, '', data[2])
                pub_date = re.sub(char, '', data[3])
                read_num = re.sub(char, '', data[4])

                comment_num = re.sub(char, '', data[5])
                # print(title, info, author, pub_date, read_num, comment_num)
                if '<div class="num">' in read_num:
                    read_num = re.search(re.compile(r'<div class="num">(.*?)</div>', re.S))
                else:
                    read_num = '0'
                if '<div class="num">' in comment_num:
                    pass
                else:
                    comment_num = '0'
                print(read_num, '---', title, info, author, pub_date, read_num, comment_num)
            self.parse_json(shown_offset)
        else:
            print('请求首页状态码异常:{}'.format(response.status_code))


    def parse_json(self, shown_offset):
        url = self.json_api.format(shown_offset)
        response = requests.get(url=url, headers=self.headers)
        if response.status_code == 200:
            json_dict = json.loads(response.text)
            articles = json_dict['articles']
            print(articles)
            offset = json_dict['shown_offset']
            print(offset)

if __name__ == '__main__':
    csdn = CSDNSpider()
    csdn.get_list()


