import requests
import random

base_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

code = ''
for i in range(0, 4):
    code = code + str(random.randint(0, 9))
    print(code)

params = {
    'apikey': '',
    'mobile': '接收人的手机号',
    'text': '',
}
