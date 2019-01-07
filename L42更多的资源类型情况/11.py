import requests
import json
import pymysql
from lxml import etree
conn = pymysql.connect(user='root', password='123456', database='jd')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS jdcomment1(content VARCHAR (500), username VARCHAR (50))')
comment_url = 'https://club.jd.com/comment/productCommentSummaries.action'
url = "https://sclub.jd.com/comment/productPageComments.action?"

params = {
    'productId':'100000287113',
    'score': 0,
    'sortType': 5,
    'page': 0,
    'pageSize': 10,
    # 'isShadowSku':0,
    # 'fold':1
    # 'callback':'fetchJSON_comment98vv15263',
}

# 伪造headers。 降低被封禁的概率。
# cookie中有jsessionid和trackid和用户名等信息，referer请求
headers = {
    'cookie': '__jdv=122270672|direct|-|none|-|1545816689735; __jdu=1911103525; PCSYCityID=412; shshshfpa=e81ca139-57b3-859d-db27-78339be22811-1545816702; user-key=e6e7b3db-b81e-4e29-8d18-2963aff81485; _pst=jd_598308d66b7f6; unick=jd_598308d66b7f6; pin=jd_598308d66b7f6; _tp=dS86tAtyZt57yHlL9R%2BNUu3v8O%2FrLAQD41K6mOOZVgg%3D; pinId=xwE-ZhW4nJSRvUbV4pUlxLV9-x-f3wj7; ipLoc-djd=1-72-2799-0; shshshfpb=hxt36K8P20YPw1TZmBAjdqQ%3D%3D; __jdc=122270672; cn=0; _gcl_au=1.1.1347703983.1545965749; 3AB9D23F7A4B3C9B=27LQVPUGGIYY62HSTBF7XSFP52OJPDLZZTFE2V3JLCCXY3FB2YGYEQRS62LZGQGPYS5HQLYJ4KMIM3UX2YXLVIDQBI; __jda=122270672.1911103525.1539428691.1545990246.1545996033.13; wlfstk_smdl=kzm0o495p17lw0iroflp4ztxhw8vfnf0; TrackID=1kVg6wrzKIkbIwtyAeS3byevhpy4PYoHZmtjXyALQiylRGYJOrvzo3iN5dZovKhbJ37a6iy5tOykVb7W7XNtTjM7FY7_zEQJ0sMnxvQI3BPA; ceshi3.com=000; shshshfp=447bcde9e37449b49000397db3ec679a; JSESSIONID=25722BAEFFFD84A72C0D98F183399A52.s1; shshshsID=94e5d0e01ba94413e0a2966cc1749b5c_10_1545997219070; __jdb=122270672.11.1911103525|13.1545996033; thor=480285E8F578B86999D37FE49A7A1F4E2ADA8E07A4BAB2F00C5E718B96CA586F9CCC3DAE4651567C4DEED22DB2E5E3E5F5638EAF8F42B2A74B54C1D995CA334B50838AA0D55C4146252ED75AE629497C8FE95F957CD05A75488DAE4679BD13A58DF869E5C8288ACFD091CFE7A6F02E38924B53AA6844C9BA3E665876FFD05AA75BEFEDBA779B1945DE5D5A2A76DF8CF9F1BC2D46DBC84ABD1799F41D5E0511A7',
    'referer': 'https://item.jd.com/100000287113.html',
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }

comment_resp = requests.get(url,params=params, headers=headers)
# print(comment_resp.status_code)
# print(comment_resp.text)
comment_str = comment_resp.text
comment_dict = json.loads(comment_str)
print('*'*80)
# print(comment_dict)

comments2 = comment_dict['hotCommentTagStatistics']
list1 = []
for comment2 in comments2:
    # print(comment2["name"])
    list1.append(comment2["name"])
print('主要优点：',list1)

comments3 = comment_dict['productCommentSummary']
print('好评度：',comments3['goodRateShow'],'%')

# s = comment_dict['productCommentSummary']['goodRateShow']
# print(s)

comments = comment_dict['comments']
xx = 1
for comment in comments:
    print(comment['id'])
    print(comment['nickname'])
    print(comment['userLevelName'])
    print(comment['content'])
    print(comment['creationTime'])
    print(comment['productColor'])
    print(comment['productSize'])
    print(comment['referenceName'])
    # print(comment['score'])
    print(' 点赞数：',comment['usefulVoteCount'])
    cursor.execute("INSERT INTO jdcomment1 VALUES (%s,%s)",[comment['content'],comment['nickname']])
    xx += 1
    # images = comment['images']
    # for image in images:
    #     print(image['imgUrl'])
conn.commit()
conn.close()

