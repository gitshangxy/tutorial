# 练习 百度关键字
"""
目标：打开浏览器，打开百度，搜索框内填充关键字，单击百度一下按钮，网页向下翻，点击第二页，打印结果列表标题。
"""
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
# 打开百度
browser.get("http://www.baidu.com")
elemt = browser.find_element_by_id("kw")
elemt.send_keys("python")
time.sleep(2)
# 百度按钮
su = browser.find_element_by_id("su")
# 点击
su.click()
# elemt.send_keys(Keys.ENTER)
# elemt.send_keys(Keys.RETURN)  # 回车
time.sleep(3)
# print(browser.find_element_by_xpath(r'//div[@class="result c-container "]//a').text())
print(browser.find_element_by_id("content_left").text)
time.sleep(5)

browser.quit()   # 关闭

# //div[@id="page"]/a