import requests
import json
from lxml import etree
import pymysql.cursors
import time


comment_url ='https://item.taobao.com/item.htm?id=578862688632&ali_refid=a3_430673_1006:1102688980:N:%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA:00b3e8307fad0d0b4bdb981f7030febb&ali_trackid=1_00b3e8307fad0d0b4bdb981f7030febb&spm=a2e15.8261149.07626516002.7'

params = {}

header = {
    'cookie': '_lastvisited=l7i5FJ3ijHQCAasPpxSBczQL%2C%2Cl7i5FJ3ijHQCAasPpxSBczQL4lKhMjT6%2Cjqls6m09%2Cjqls6m09%2C3%2C5726fad4%2Cl7i5FJ3ijHQCAasPpxSBczQL%2Cjqlsx24j; _uab_collina=154683258604256073498853; _umdata=70CF403AFFD707DFF3E95395CD8A6FFBFED9813921568EB1780AC32782D7440069DAB387A094176ACD43AD3E795C914C35CD98E12D01C81D774A9D5DD3596788',
    'referer': 'https://item.taobao.com/item.htm?id=578862688632&ali_refid=a3_430673_1006:1102688980:N:%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA:00b3e8307fad0d0b4bdb981f7030febb&ali_trackid=1_00b3e8307fad0d0b4bdb981f7030febb&spm=a2e15.8261149.07626516002.7',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

comment_resp = requests.get(url=cmment_url, params=params, header=header)







"""
Cookie: cna=l7i5FJ3ijHQCAasPpxSBczQL; sca=bcf97b5b; cdpid=UNQ2k6288PGAuQ%253D%253D; cnaui=3413193979; aui=3413193979; atpsidas=5a2f4afb18b244170776d6a9_1546833769_15; tbsa=0c08247a88ffa458fffd926c_1546833769_16; atpsida=ced305c4f7adad943f621c68_1546833769_17

https://item.taobao.com/item.htm?id=578862688632&ali_refid=a3_430673_1006:1102688980:N:%E5%B0%8F%E7%B1%B3%E6%89%8B%E6%9C%BA:00b3e8307fad0d0b4bdb981f7030febb&ali_trackid=1_00b3e8307fad0d0b4bdb981f7030febb&spm=a2e15.8261149.07626516002.7
"""


