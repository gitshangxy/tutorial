import requests
# LWPCookieJar()可以自动将响应头中Set-Cookie中的值保存下来，不需要在单独解析了。
from http.cookiejar import LWPCookieJar

class LoginSpider(object):
    def __init__(self):
        self.url = 'http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr'
        self.session = requests.Session()
        self.session.cookies = LWPCookieJar(filename='cookies.txt')

    def index(self):
        """
        请求首页url，获取学员的信息
        :return:
        """
        # 在访问这个首页的时候，先从本地文件cookies.txt读取登录之后的cookie信息。如果本地cookie文件不存在，那么需要先登录cookie
        try:
            self.session.cookies.load(filename='xxx.txt', ignore_expires=True, ignore_discard=True)
            response = self.session.get(url='http://kaoshi.zhiyou900.com:8888/edustu/me/edu/meda.spr')
            if response.status_code == 200:
                print(response.text)
            else:
                # 可能是cookie不能使用了，此时需要重新登录，生成新的cookie信息，并保存在cookies.txt
                result = self.login()
                if result == 'ok':
                    self.index()
        except Exception as e:
            # 本地文件不存在，此时在进行模拟登录
            print('Cookie加载失败')
            result = self.login()
            if result == 'ok':
                self.index()

    def login(self):
        """
        模拟登录函数。
        :return:
        """
        print('开始登录')
        login_url = 'http://kaoshi.zhiyou900.com:8888/edustu/login/login.spr'
        post_data = {
            'j_username': '15516338825',
            'j_password': '123456'
        }
        # 这个POST请求主要就是为了Set-Cookie，但是self.session会自动解析这些Cookie，并保存起来。
        response = self.session.post(url=login_url, data=post_data)
        if response.status_code == 200:
        # 登录成功，将登陆之后的所有的Cookie保存在cookies.txt文件中
            self.session.cookies.save(ignore_discard=True, ignore_expires=True)
            return 'ok'
        else:
            return 'error'


if __name__ == '__main__':
    obj = LoginSpider
    obj.index()
