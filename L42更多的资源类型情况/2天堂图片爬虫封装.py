# 需求  1. 封装成函数
# 2. 加入代理
import requests
import re
import json
from lxml import etree

# 蘑菇代理获取地址
MOGU_PROXY_URL = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=fc1a46b572d54ca0a12f375eceb3b5e8&count=20&expiryDate=0&format=1&newLine=2'
FPEE_PROXY_URL = 'http://192.168.221.221:5010/get'

def get_proxies():
    """
    请求付费代理
    :return:
    """
    try:
        response = requests.get(MOGU_PROXY_URL)
    except Exception as e:
        print("获取代理失败", e, response.status_code)
    if not response.status_code == 200:
        resp_dict = json.loads(response.text)
        proxies = resp_dict['msg']
        # 组装resquests包代理参数需要的格式
        res_proxies = []
        for proxy in proxies:
            # proxy_type = 'https'
            # proxy_url = 'https://' + proxy['ip'] + proxy['port']
            return proxies

print(get_proxies())

proxies = {
    "http": "http://14.118.135.10:8080",
}

# response = requests.get(url, proxies=proxies)



# def get_free_proxies():
#     i = 1
#     while True:
#         try:
#             print('第{}次尝试获取代理'.format(i))
#             resp = requests.get(FPEE_PROXY_URL)
#             i += 1
#
#             proxy_url = 'http://' + resp.text
#             proxies = {'http':proxy_url}
            # resp2 = requests.get(TIANTANG_INDEX_URL, proxies=proxies, time)