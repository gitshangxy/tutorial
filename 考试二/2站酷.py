import urllib.request
from lxml import etree

response = urllib.request.urlopen('https://www.zcool.com.cn/work/ZMzI2MTMwNDQ=.html')
# print(response)  # 查看响应度信息
# print(response.code)   # 响应200
html_content = response.read()
# print(html_content)   # 字节类型的网页
content_html = html_content.decode(encoding='utf-8')   # 字节编码成字符串，输出网页html源代码
# print(content_html)
# 解析
html = etree.HTML(content_html)

# li[@class="menu-list hide"]/p/a')
content_rasp = html.xpath('//div[@class="card-img"]/a')
# print(content_rasp)

# //div[@class="work-list-box clear"]/div[@class="card-img"]/a/img