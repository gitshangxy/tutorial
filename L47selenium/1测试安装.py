from selenium import webdriver
import time

# 生成浏览器实例。根据环境找到chromedriver.exe进而驱动chrome.exe
browser = webdriver.Chrome()
browser.get("http://www.baidu.com")
time.sleep(6)
browser.quit()   # 关闭退出

