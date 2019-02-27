"""
思路：
1. 获得验证码图片；
2. 将这个验证码图片保存到本地，同时将这个图片上传至云打码平台进行识别
"""

import requests, json


class YDMSpider(object):


    def __init__(self):
        self.session = requests.Session()
        # self.session.cookies = LWPCookieJar(filename='zhihu.txt')
        self.headers = {}
        pass

    def login(self):
        content = self.session.get(url='', headers=self.headers).content
        with open('captcha.png', 'wb')as f:
            f.write(content)


