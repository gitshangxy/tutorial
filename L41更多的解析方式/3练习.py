
# 练习 http://example.python-scraping.com/places/default/view/United-States-234
# 分别用正则、bs、xpath解析,命令行输出国家名country、相邻国家名neighbours

import requests
import re
from lxml import etree
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 请求
url = 'http://example.python-scraping.com/places/default/view/United-States-234'
headers = {
    'UserAgent': UserAgent().random
}
response = requests.get(url=url, headers=headers)
if not response.status_code == 200:
    raise Exception(f"请求失败, {response.status_code}")
html_content = response.text

# init
tree = etree.HTML(html_content)
bs = BeautifulSoup(html_content, 'lxml')

# pattern
pattern_re = re.compile(r'<tr id="places_country_or_district__row">.*?<td class="w2p_fl">.*?</td><td class="w2p_fw">(.*?)</td>', re.S)
pattern_xpath = '//tr[@id="places_country_or_district__row]/td[@class="w2p_fw"]/text()'

# regex
re_result = pattern_re.findall(html_content)
print(re_result[0])

# xpath
x = '//*[@id="places_country_or_district__row"]/td[2]/text()'
country = tree.xpath(x)
print(f'国家{country}')

# bs
tag_tr = bs.find(id="places_country_or_district__row")
tag_td = tag_tr.find('td', {'class': "w2p_fw"})
print(tag_td.string)


