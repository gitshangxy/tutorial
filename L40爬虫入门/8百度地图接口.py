import urllib.request
import urllib.parse
import json

origin_args = {'query': 'ATM机', 'region': '郑州', 'output': 'json', 'ak': 'q9AjUitghvqRsBdnApImtMRcro6SEfKc'}
# 将中文参数base64编码
b64_args = urllib.parse.urlencode(origin_args)
print(b64_args)
base_url = 'http://api.map.baidu.com/place/v2/search'
url = base_url + '?' + b64_args
print('拼好的url', url)

resp = urllib.request.urlopen(url)
content_json = resp.read().decode()
print(content_json)
# json转对象
content_obj = json.loads(content_json)
print(content_obj)
results = content_obj['results']
for row in results:
    print(row['name'], row['address'])




# http://lbsyun.baidu.com/