# 练习1  纯静态网页获取纯文本 https://news.163.com/  获取头条部分信息。

import requests
from lxml import etree
from fake_useragent import UserAgent

url = 'https://news.163.com/'
headers = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
if not response.status_code == 200:
    raise Exception(f"请求失败, {response.status_code}")
html_content = response.text

tree = etree.HTML(html_content)

# 每条新闻的头部
x1 = '//*[@id="js_top_news"]//a/text()'
# 网站的头部
x2 = '//div[@class="ns_area list"]//a/text()'
country = tree.xpath(x1)
country2 = tree.xpath(x2)


# 第二种方法
url2 = 'https://news.163.com/'
response = requests.get(url2)
if response.status_code != 200:
    raise Exception(f"请求失败")
html_content = response.text
# 二进制 resp.content     resp.text  自动编码后的字符串
# 偶尔resp.text自动解码信息错误、中文乱码。 resp.content.decode(encoding='网站编码类型')

pattern1 = '//div[@class="mod_top_news2" and @id="js_top_news"]/h2/a/text()'
pattern2 = '//div[@class="mod_top_news2" and @id="js_top_news"]/ul[@class="top_news_ul"]/li/a/text()'

etree = etree.HTML(html_content)
new1 = etree.xpath(pattern1)
new2 = etree.xpath(pattern2)

for i in new1: print(i)
for j in new2: print(j)

# xpath尝试思路
# xpath没有匹配到想要尝试的东西'//div[@class="mod_top_news2" and @id="js_top_news"]/h2/a/text()',不断缩短xpath表达式，看前面的标签有没有匹配到。
