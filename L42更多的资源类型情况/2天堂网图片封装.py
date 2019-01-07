
import os
from urllib.request import Request, urlopen, urlretrieve
import requests
from lxml import etree

if not os.path.exists('imgs'):
    os.mkdir('imgs')    # 创建文件夹
    os.chdir('imgs')    # 切换当前文件夹

page_number = 1

def get_page_code(url):
    global page_number
    content = requests.get(url).content
    print(type(content))
    html_obj = etree.HTML(content)
    print(html_obj)


    img_list = html_obj.xpath('//div[@class="il_img"]/a/img')
    print('正在下载第{}页'.format(page_number))
    os.mkdir(str(page_number))
    os.chdir(str(page_number))

    for img in img_list:
        img_src = img.xpath('@src')[0]
        img_alt = img.xpath('@alt')[0]
        urlretrieve(img_src, img_alt+'.jpg')
    # for循环外面页码+1
    page_number += 1
    os.chdir(os.path.pardir)

    next_page_obj = html_obj.xpath('//a[@class="page-next"]')
    if len(next_page_obj) == 0:
        print('没有下一页')
        return

    a_obj = next_page_obj[0]
    href = a_obj.xpath('@href')[0]
    url = 'http://www.ivsky.com' + href
    # 在函数内部调用自身称为递归调用
    get_page_code(url)

get_page_code('http://www.ivsky.com/tupian/ziranfengguang/')