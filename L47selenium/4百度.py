# 模拟登陆百度
from selenium import webdriver
from time import sleep
import time

# 新建webdriver对象
driver = webdriver.Chrome()
driver.get('https://passport.baidu.com/v2/?login')
time.sleep(2)
elemt = driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn")
elemt.click()
user = driver.find_element_by_name("userName")
user.send_keys("liskysxy")
time.sleep(2)
password = driver.find_element_by_name("password")
password.send_keys("199844lucky")
time.sleep(2)
dl = driver.find_element_by_id("TANGRAM__PSP_3__submit")
dl.click()
time.sleep(2)

driver.quit()














#
# driver.find_element_by_id("TANGRAM__PSP_3__footerULoginBtn").click()
# driver.find_element_by_name("userName").clear()
# driver.find_element_by_name("userName").send_keys('注冊什么id好呢')
# driver.find_element_by_name("password").clear()
# driver.find_element_by_name("password").send_keys('56Tyghbn')
# sleep(2)
#
# # 获取验证码
# code_img_src = driver.find_element_by_id("TANGRAM__PSP_3__verifyCodeImg").get_attribute('src')
#
# sleep(10)
# driver.find_element_by_id("TANGRAM__PSP_3__submit").click()
# print(driver.get_cookies())