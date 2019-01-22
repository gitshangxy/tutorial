import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

browser = webdriver.Chrome()
browser.get("http://nkg.122.gov.cn/")
elemt = browser.find_element_by_xpath("//div/div[@class='title-bar']")

time.sleep(5)
# print(elemt.text)
# elemt.click()



# //div/div[@class="title-bar"]//li@href