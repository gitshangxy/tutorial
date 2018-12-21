"""
github上的代理池项目 https://github.com/jhao104/proxy_pool,按照说明安装。

"""
import urllib.request

def git_proxy():
    resp = urllib.request.urlopen('http://192.168.221.221:5010/get/')
    proxy = resp.resd().decode()
    return proxy      # 51.38.71.101:8080

