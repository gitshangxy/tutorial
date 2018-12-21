import re
import requests
from lxml import html
# from pymongo import MongoClient

# client = MongoClient()
# db = client['豆瓣']
# collection = db['豆瓣新书']
html2 = requests.get('https://book.douban.com/').content.decode()

# 正则表达式
# pattern1 = '<h4 class="title">(.*?)</h4>.*?<span class="author">(.*?)</span>'
# selector = re.findall(pattern1, html2, re.S)
# content = re.search(pattern1, html2, re.S).group(1,2)
# print(selector)
# print(len(selector))

# for i in selector:
#     aa = re.sub('[\n ]', '', i[0])
#     bb = re.sub('[\n ]', '', i[1])
#     print(f'书名：{aa}\t作者{bb}')
    # collection.insert_one({'书名': aa, '作者': bb})


se = html.fromstring(html2)
x = se.xpath('//*[@id="content"]/div/div[1]/div[1]/div[2]/div/div/ul/li/div/div//a/text()')
print(x)
author = se.xpath('//div[@class="slide-list"]/ul/li/div//div[@class="author"]/text()')
list1 = []
for n in author:
    a = re.sub('[\n ]', '', n)
    list1.append(a)
print(list1)
print(author)