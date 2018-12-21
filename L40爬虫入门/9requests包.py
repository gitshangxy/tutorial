# requests包
# urllib偏底层    参数编码，修改useragent或使用proxy时需要几行代码来进行构造操作，获得响应后需要读数据和解码。所以我们使用更加方便的requests包。

import requests

# GET请求  无参数
# response = requests.get('http://www.baidu.com')
# print(response.status_code)
# print(response.content)      # content  二进制原始数据
# print(response.text)      # 解码后的字符串

# 有参数  requests包会自动把参数base64转码
resp = requests.get('http://www.baidu.com', params={'kw': '学习'})
print(resp.url)
print(resp.text)

# 添加自定义请求头信息headers
headers = {
    'User_Agent': ''    # 上课随机useragent的值填过来
}
requests.get('www.baidu.com', headers=headers)

# post
params = {'username': '小红', 'address': '郑州'}
requests.post('https://www.baidu.com', params=params)

# 代理
proxies = {
    'http': 'http://{}:{}'.format('185.132.133.107', '8571')
}
requests.get('www.baidu.com', headers=headers, proxies=proxies)

