# 练习 L42节3github模拟登录改类封装
# 函数封装和类封装并没有孰优孰劣，函数封装思维自然， 类封装程度更高，django框架函数封装、odoo框架类封装。类封装访问公共变量较方便。

import requests
from lxml import etree

class Github(object):
    def __init__(self):
    # 属性，公共变量  配置项  全局需要访问
        self.login_url = 'https://github.com/login'
        self.do_login_url = 'https://github.com/session'
        self.profile_url = 'https://github.com/settings/emails'
        self.headers = {
            'Host': 'github.com',
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}
        self.s = requests.Session()

    def get_csrf_token(self):
        # 请求表单页
        resp = self.s.get(self.login_url)
        html_content = resp.text
        pattern = '//input[@name="authenticity_token"]/@value'
        dom = etree.HTML(html_content)
        authenticity_token = dom.xpath(pattern)[0]
        # return authenticity_token
        self.do_login(authenticity_token)


    def do_login(self,authenticity_token):
        session_args = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': authenticity_token,
            'login': '2765970564@qq.com',
            'password': '199844lucky'
        }

        resp = self.s.post(self.do_login_url, headers=self.headers, data=session_args)
        if resp.status_code != 200:
            raise Exception("请求登陆结构失败{}".format(resp.status_code))
        print("登录成功")
        # return True
        self.request_profile()


    def request_profile(self):
        # 请求个人页
        resp = self.s.get(self.profile_url, headers=self.headers)
        if resp.status_code != requests.codes.ok:
            raise Exception("请求个人设置页失败")
        print("请求个人设置页成功")
        profile_html_content = resp.text
        # print(profile_html_content)
        # return profile_html_content
        self.get_user_name(profile_html_content)


    def get_user_name(self, profile_html_content):

        pattern_profile_email = '//select[@id="primary_email_select"]/option/text()'
        profile_dom = etree.HTML(profile_html_content)
        profile_email = profile_dom.xpath(pattern_profile_email)[0]
        print(profile_email)

        # pattern_profile_email = '//select[@id="primary_email_select"]/option/text()'
        # profile_dom = etree.HTML(profile_html_content)
        # profile_email = profile_dom.xpath(pattern_profile_email)
        # print(profile_email)
        # print('最终信息', profile_email)

# if __name__ == '__main__':
#     github = Github()
#     authenticity_token = github.get_csrf_token()
#     github.do_login(authenticity_token)
#     profile_html_content =github.request_profile()
#     github.get_user_name(profile_html_content)

content=Github()
content.get_csrf_token()