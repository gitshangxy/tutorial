"""
介绍：
负责的异步逻辑,js方法,参数签名,各种csrf token  session token并不容易梳理出流程。那么就直接用浏览器。
过时的：phantomjs  无头浏览器。
"""

from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
time.sleep(6)
browser.quit()   # 退出浏览器



"""
1. 下载对应平台版本，保证驱动跟浏览器大版本一致。
官网下载 http://chromedriver.storage.googleapis.com/index.html
国内镜像 http://npm.taobao.org/mirrors/chromedriver/
2. 放到chrome.exe放在同一目录下
3. chrome根目录配置到环境变量中，刷新环境变量或重启。
4. 关闭所有chrome浏览器或重启电脑已生效。

可能出现的异常：
第3步后仍报 chromedriver文件需要放到环境变量中，而环境变量已经配好和生效。这是因为chrome未重启跟驱动建立联系。
"""