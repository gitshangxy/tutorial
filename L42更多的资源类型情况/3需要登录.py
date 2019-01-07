# 3. 需要登录的情况
"""
场景：
解决方式：用户登录
"""

"""
需求：模拟登录，获取github 个人页/email/   登录邮箱。

分析：直接访问个人页会重定向到登录页。
1. 请求登录页，接收sessionid存入cookie
1) 先通过谷歌开发者工具找到login的请求（类型、url、参数）。刷新登录页，然后clear请求，然后点击登录页，观察新出现的请求。
2) 分析去登录这个请求
路由， https://github.com/sessing
方法，post
参数，commit: Sign in
    utf8: ✓
    authenticity_token: 3ti65iO65iZd+Q7n3N1Er4VKEbl8MtyoRdZGgxK+Lc5eRN5oPzDHJ4TYmrOK9JTkg3/47/v3ANfly5lKbzYMhQ==
    login: 2765970564@qq.com
    password: xxx
    注意authenticity_token跟cookie中的user_session不一样。authenticity_token是请求https://github.com/login登录页时的CSRF token，为了防止表单传出过程中被截取伪造。
    user_session是登录成功后服务器返回的token，代码已经登录。

2. 请求个人页（携带cookie）
3. 请求个人页（requests请求个人页成功后才发现），github个人设置页时返回完整的

梳理步骤
1. get请求 login页面
2. xpath把login页面authenticity_token获取下来获取cookie
3. 去登陆，准备好各个参数。
4. post请求  去登录  session 第3步的参数 cookie
5. get请求 个人页
6. xpath个人页邮箱给取出

小技巧：请求获取到的源代码粘贴到空的html文件
"""

import requests
import getpass
from lxml import etree

login_url = 'https://github.com/login'
do_login_url = 'https://github.com/session'
profile_url = 'https://github.com/settings/emails'

# 未登录是请求个人页  会重定向 返回index登录表单HTML数据。
# profile_resp = requests.get(profile_url)
# print(profile_resp.status_code, profile_resp.text)

headers = {
    'Host': 'github.com',
    'Referer': 'https://github.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

# requests Session会话。优点：1保持会话，管理cookie 2重用底层tcp连接同一网址提升效率
s = requests.Session()
login_resp = s.get(login_url, headers=headers)
if login_resp.status_code != 200:
    raise Exception("get请求登录页表单失败{}".format(login_resp.status_code))
login_html_content = login_resp.text

# print(login_resp.text)

# 获取表单的csrf token
login_dom = etree.HTML(login_html_content)
pattern_authenticity_token = '//input[@name="authenticity_token"]/@value'
authenticity_token = login_dom.xpath(pattern_authenticity_token)[0]
print(authenticity_token)

# 请求登录接口
# 准备所需参数
# password = getpass.getpass("请输入密码:")
session_args = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': '2765970564@qq.com',
    'password': '199844lucky'
}
# getpass.getpass("请输入密码:")
session_resp = s.post(do_login_url, headers=headers, data=session_args)
if session_resp.status_code != 200:
    raise Exception("请求登录接口失败{}".format(session_resp.status_code))
print("登录成功")
# 请求成功后 会话id user_token或(session)会写入到requests的cookie管理器中，以后的请求会携带上，从而保持登录状态

# 请求个人设置页
profile_resp = s.get(profile_url, headers=headers)
if profile_resp.status_code != requests.codes.ok:
    raise Exception("请求个人设置页失败")
# print(profile_resp.text)
# 获取邮箱
# 账户名登录的 select标签id和邮箱登录的不一致，根据变化修改xpath
pattern_profile_email = '//select[@id="primary_email_select"]/option/text()'
profile_dom = etree.HTML(profile_resp.text)
profile_email = profile_dom.xpath(pattern_profile_email)[0]
print('最终信息', profile_email)




"""
# 作业：
复习刚才示例的操作和分析过程
百度阅读CSRFtoken的作用和中间人攻击。
百度阅读会话token的作用和生成原理。
自己动手再分析一遍

1. github登录页
2. 在登录页源代码找到csrftoken
3. 点击登录，开发者工具中找到去登录的请求，找到请求体重的form数据
4. 登陆后查看开发者工具application中的cookie，找到会话token。
"""
