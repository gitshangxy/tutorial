# urllib包，专门处理http请求响应的内置包。
# import urllib   # urllib包下的__init__.py没写东西，import urllib写法并不会引入其他文件。

import urllib.request  # from urllib import request
# from urllib.request import urlopen
response = urllib.request.urlopen('http://www.baidu.com')  # 建议debug看response里的信息
# urlopen(url,
#
# data={参数1: 值1, 参数2: 值2,}, timeout=网页响应超时时间)
# print(response)   # <http.client.HTTPResponse object at 0x0000015D80912518>
# 从响应度信息
# print(response.code) # 响应 200
html_content = response.read()  # socketIO bufferReader 模式rb，从响应体中读网页信息二进制数据出来。
# print(html_content)   # 字节类型的网页信息
print(html_content.decode(encoding='utf-8'))  # 字节解码成字符串 获得html文件



"""
# 网上教程urllib urllib2，urllib3
# python2，3时代内置处理http的包是urllib。增加改进发布urllib2包。这两个包都是内置。
# urllib3第三方开发者开发，语法比较自然，requests包基于urllib3包。
# python3时代把python2时代的urllib、urllib2包合并成urllib。
# 总结：现在我们用的http相关处理包，主要有内置的urllib，第三方requests这两个包。urllib包稍微偏底层，代码稍麻烦但理清楚; requests封装良好使用简单。
"""

