# grequests
# 由gevent  greenlet  requests合并组成的异步请求包。封装程度较高，不需要关注协程书写。
# pip install grequests
# ctrl + alt + O
import grequests
import requests
import time

urls = [
    'http://pic1.cxtuku.com/00/10/86/b3409096f4a2.jpg',
    'http://5b0988e595225.cdn.sohucs.com/images/20181217/86383c900ccc41af82aadbbe9bf40f7d.jpeg',
    'http://pic31.nipic.com/20130720/5793914_122325176000_2.jpg',
    'http://www.baidu.com',
    'http://www.douban.com',
    'https://github.com'
]

# 同步
# start_time = time.time()
# for url in urls:
#     try:
#         resp = requests.get(url)
#         print(resp.status_code)
#         if resp.status_code == 200:
#             print(resp.text)
#     except Exception as e:
#         print(e)
# end_time = time.time()
# print(end_time - start_time)


# 异步请求
# url列表准备成一个个requests请求对象，以生成器返回，这个生成式每次返回一个 requests.get(url) 对象。这时还未真正请求。get()方法与requests包的get()方法一致，可以加params、timeout等参数。
start_time = time.time()
rs = (grequests.get(url) for url in urls)
# 同时请求
# map()方法 接收上面的生成器，每次取出一个requests.get(url)请求，接收requests，最终返回所有requests。非阻塞所有请求同时发送，并不是因为某一个请求没有得到requests还停止其它工作。resp_list已最慢请求为准，默认40s超时
resp_list = grequests.map(rs)
# 拿到所有请求响应后就可以方便地循环取值，resp的顺序与urls一致。
for resp in resp_list:
    if resp is None:
        print(resp.url, '请求失败')
    else:
        print(resp.status_code)
        print(resp.content)
end_time = time.time()
print(end_time - start_time)

"""
可能出现的错误: 
MonkeyPatchWarning:
解决方法： 看一下grequests包是否在requests之上
"""

"""
urls = [1,2,3,4]
a = [url for url in urls] 
print(a, type(a))   →  [1, 2, 3, 4]  <class list>

b = (url for url in urls) 
print(type(b))→ <generator object <genexpr> at 0x0000013CADE36728>
相当于
def foo():
for url in urls:
        yield uel
b = foo()
"""
# scrapy