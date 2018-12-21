# urllib代理示例
# 为了防止同一个ip频繁访问服务器被封锁，需要不断变化ip通过别人的电脑代理访问服务器。

"""
从哪找代理？
1. ip代理平台 http://www.xicidaili.com/nn/
免费的不太稳定有些不可用。付费的稳定。
2. 网友搜集爬取的ip代理池。

"""
import urllib.request

# 设置代理操作器
proxy = urllib.request.ProxyHandler({'http': 'http://110.84.208.56:8118'})
# 构建新的请求器，覆盖默认opener
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
response = urllib.request.urlopen('http://www.baidu.com/s?wd=ip')
html_content = response.read().decode('utf-8')
print(html_content)



"""
可能出现的错误
1 长时间未响应 。 urllib.error.URLError: <urlopen error [WinError 10060]
"""
