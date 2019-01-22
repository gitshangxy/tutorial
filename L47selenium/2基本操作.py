from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# 打开、退出浏览器，请求网页
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# time.sleep(5)
# driver.quit()

# 打开本地html测试网页
# 无头模式
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# browser = webdriver.Chrome(chrome_options=chrome_options)
# 普通模式
browser = webdriver.Chrome()
browser.get('file:///D:/pycharm尚小雨/tutorial/L47selenium/2index.html')   # 绝对路径
time.sleep(2)
# # browser = webdriver.Firefox()
# browser.get("https://3416230579.github.io/page/index.html")


# 1>（常用）根据id或name获取标签，打印标签属性、文本
# 实质上也是先lxml转换成文档树。 语法类似xpath、bs、js         getElementById('')    getElementsByName('')
# 根据 id 获取对象   根据 name 获取对象
elemt = browser.find_element_by_id("element_id")
# print(elemt)
elemt2 = browser.find_element_by_name("element_id")
print(elemt)

# 2>取标签中值、属性
print(elemt.text)       # 标签内容
# print(browser.find_element_by_name().text)
print(elemt.get_attribute('id'))    # 取属性

# 3>给标签输入文本  elemt_obj.inner_text='new text'
elemt.send_keys("自动填充一些内容")
time.sleep(2)

# 4> (了解)根据标签内容选择标签
elemt = browser.find_element_by_link_text("find_element_by_link_text")
print(elemt.tag_name)   # 打印标签名
elemt.click()    # (常用)鼠标单击
time.sleep(2)

# 5> (了解)根据css选择器语法查找标签
# 页面A 上连接打开了页面B，焦点在页面B，但不影响获取页面A元素。
elemt = browser.find_element_by_css_selector(".highlight")
elemt.send_keys("啦啦啦")  # 网页的焦点并没有移动到新标签页上。
time.sleep(2)

# 6>（常用）根据 xpath选择元素
elemt = browser.find_element_by_xpath(r'//*[@id="xpathname"]')
elemt.send_keys("根据 xpath")
time.sleep(2)

# 7>(常用)切换标签页，获取页面源代码
browser.switch_to.window(browser.window_handles[0])
print(browser.page_source)
time.sleep(2)

# 8>跳转到弹窗，点击确定
# 操作弹出框
elemt = browser.find_element_by_tag_name("button")
elemt.click()
time.sleep(2)
browser.switch_to.alert.accept()  # 切换到弹出框操作


# 9>跳转和回退操作
elemt = browser.find_element_by_link_text("forward_back")
elemt.click()  # 点击跳转
time.sleep(1)
browser.back()
time.sleep(1)
browser.forward()
time.sleep(1)

# 10>cookies  待测试
# print(browser.get_cookies())
# # 添加一个 cookie
# browser.add_cookie({"name":"testselenium", "domian":"www.baidu.com"})
# print(browser.get_cookies())

# 11>键盘特殊按键    elemt.send('asdf')  elemt.click()
# elemt.send_keys(Keys.RETURN)   # Keys.ENTER

browser.quit()    # 关闭

"""
（了解）无头浏览器模式
无头模式：浏览器后台运行，并不展示窗口页面，有利于节省资源提升速度。

"""

# 参考：虫师的博客

# 报错
# 1. selenium.common.exceptions.WebDriverException: Message: unable to set cookie
#   (Session info: chrome=71.0.3578.98)
#   (Driver info: chromedriver=71.0.3578.80 (2ac50e7249fbd55e6f517a28131605c9fb9fe897),platform=Windows NT 10.0.17134 x86_64)
# 参考：https://www.jianshu.com/p/a1a64f649472