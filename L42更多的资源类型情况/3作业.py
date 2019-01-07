# 学习csv文件存储和爬取京东商品。cookie从登陆成功的浏览器里复制。
# 没写好
import requests
import csv
from lxml import etree

# login_url = 'https://passport.jd.com/new/login'
#
# url = 'https://search.jd.com/Search?keyword=%E9%A6%99%E6%B0%B4&enc=utf-8&wq=%E9%A6%99%E6%B0%B4&pvid=4357797e797d497685051886cf65ce23'

# requests = requests.get(login_url)
# print(requests.status_code, requests.text)

def resp_file(n):
    url = 'https://search.jd.com/Search?keyword=%E9%A6%99%E6%B0%B4&enc=utf-8&suggest=3.his.0.0&wq=&pvid=3cfd65b2e0b94baa8949ae2fe62b71bd'

    head = {
        'authority': 'search.jd.com',
        'method': 'GET',
        'path': '/ im.php?r = 1899136819 & t = 1545918972.6841 & cs = 9a87eb3f88075636b3c7126a91a18ca3',
        'scheme': 'https',
        'referer': 'https://search.jd.com/Search?keyword=%E9%A6%99%E6%B0%B4&enc=utf-8&suggest=3.his.0.0&wq=&pvid=3cfd65b2e0b94baa8949ae2fe62b71bd',
        'user - agent': 'Mozilla / 5.0(Windows NT 6.1;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 70.03538.102Safari / 537.36',
        'x-requested-with': 'XMLHttpRequest',
        'cookie': '__jdc=122270672; __jdv=122270672|direct|-|none|-|1545816689735; __jdu=1911103525; PCSYCityID=412; shshshfpa=e81ca139-57b3-859d-db27-78339be22811-1545816702; user-key=e6e7b3db-b81e-4e29-8d18-2963aff81485; _pst=jd_598308d66b7f6; unick=jd_598308d66b7f6; pin=jd_598308d66b7f6; _tp=dS86tAtyZt57yHlL9R%2BNUu3v8O%2FrLAQD41K6mOOZVgg%3D; pinId=xwE-ZhW4nJSRvUbV4pUlxLV9-x-f3wj7; cn=14; ceshi3.com=000; TrackID=1wVRnQ1JsaU6iWXoSq9zXRaaq_fsI9ZgymtsBVrG4EV-t6yU7s6A5hTXHbKmR7leznyEafQOhEpFgVuVdFg3iAIFx7l1d7jOrL536koS5S3g; xtest=7976.cf6b6759; ipLoc-djd=1-72-2799-0; shshshfpb=ik5W7AtRITDGRbOjfITWe%2Bg%3D%3D; rkv=V0400; qrsc=3; __jda=122270672.1911103525.1539428691.1545914519.1545918373.5; __jdb=122270672.4.1911103525|5.1545918373; shshshfp=52aa3e857a6aee716836d331710dd386; shshshsID=9c3da9b6bd7be26349e50bee037f50f1_4_1545918956419; thor=553C2442713C9B5019CF976CB722CB802EE2045C46FF2A7B3BE4E91BFBDC164E4524644BFFAEDD6F114D52E6868092708D4886E94F707B6E302B5520A7EB917EF8A00F94519D5FF9D29F309DAB6D79339360DFB467C10FCC8131888C9E5B4B46BADABE54B2D2BC21EE73CCC9961E414BE692C79EA64389754757F43D551DE57278BAC5D03CB48A6994B84BF894FE5F15C78F5D0D8E9B906B2D2500396A1E1F4E'
    }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    datas = html1.xpath('//ul[@class="gl-warp clearfix"]/li')
    # print(datas)
    with open('JD_Phone.csv', 'a', newline='', encoding='utf-8')as f:
        write = csv.writer(f)
        for data in datas:
            # 价格
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            # 评价
            p_comment = data.xpath('div/div[@class="p-commit"]/strong/a/text()')
            # 名字
            p_name = data.xpath('div/div[@class="p-name p-name'
                                '-type-2"]/a/em/text()')

            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-done="1"')
                # xpath('string(.)')用来解析混夹在几个标签中的文本
            write.writerow([p_name[0].xpath('string(.)'), p_price[0], p_comment[0]])
            f.close()
# requests = requests.get(resp_file(n))
