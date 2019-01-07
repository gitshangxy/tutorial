# 京东评论写数据库
import requests
import json
from lxml import etree
import pymysql.cursors
import time


def get_comments(product_id=None, page=None, page_size=10):
    """
    取评论
    :return: [[id,username,score,], []]或 [{'id':123123, 'username': 'zzdxyz', 'score': 5}]
    """
    comment_url = 'https://sclub.jd.com/comment/productPageComments.action'

    params = {
        'productId': product_id,  # 商品id。先写死 苹果手机。
        'score': 0,
        'sortType': 5,
        'page': page,
        'pageSize': page_size,
        # 'callback': 'fetchJSON_comment98vv15261',
        # 'isShadowSku': 0,
        # 'fold': 1
    }

    # 伪造headers。 降低被封禁的概率。
    # cookie中有jsessionid和trackid和用户名等信息。referer请求前的页面地址。useragent浏览器标识。
    headers = {
        'cookie': '__jdv=122270672|direct|-|none|-|1545816689735; __jdu=1911103525; PCSYCityID=412; shshshfpa=e81ca139-57b3-859d-db27-78339be22811-1545816702; user-key=e6e7b3db-b81e-4e29-8d18-2963aff81485; _pst=jd_598308d66b7f6; unick=jd_598308d66b7f6; pin=jd_598308d66b7f6; _tp=dS86tAtyZt57yHlL9R%2BNUu3v8O%2FrLAQD41K6mOOZVgg%3D; pinId=xwE-ZhW4nJSRvUbV4pUlxLV9-x-f3wj7; ipLoc-djd=1-72-2799-0; shshshfpb=hxt36K8P20YPw1TZmBAjdqQ%3D%3D; __jdc=122270672; cn=0; _gcl_au=1.1.1347703983.1545965749; 3AB9D23F7A4B3C9B=27LQVPUGGIYY62HSTBF7XSFP52OJPDLZZTFE2V3JLCCXY3FB2YGYEQRS62LZGQGPYS5HQLYJ4KMIM3UX2YXLVIDQBI; __jda=122270672.1911103525.1539428691.1545990246.1545996033.13; wlfstk_smdl=kzm0o495p17lw0iroflp4ztxhw8vfnf0; TrackID=1kVg6wrzKIkbIwtyAeS3byevhpy4PYoHZmtjXyALQiylRGYJOrvzo3iN5dZovKhbJ37a6iy5tOykVb7W7XNtTjM7FY7_zEQJ0sMnxvQI3BPA; ceshi3.com=000; shshshfp=447bcde9e37449b49000397db3ec679a; JSESSIONID=25722BAEFFFD84A72C0D98F183399A52.s1; shshshsID=94e5d0e01ba94413e0a2966cc1749b5c_10_1545997219070; __jdb=122270672.11.1911103525|13.1545996033; thor=480285E8F578B86999D37FE49A7A1F4E2ADA8E07A4BAB2F00C5E718B96CA586F9CCC3DAE4651567C4DEED22DB2E5E3E5F5638EAF8F42B2A74B54C1D995CA334B50838AA0D55C4146252ED75AE629497C8FE95F957CD05A75488DAE4679BD13A58DF869E5C8288ACFD091CFE7A6F02E38924B53AA6844C9BA3E665876FFD05AA75BEFEDBA779B1945DE5D5A2A76DF8CF9F1BC2D46DBC84ABD1799F41D5E0511A7',
        'referer': 'https://item.jd.com/100000287113.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    }

    comment_resp = requests.get(url=comment_url, params=params, headers=headers)
    print(comment_resp.status_code)
    comment_str = comment_resp.text

    comment_dict = json.loads(comment_str)
    # comment_dict = json.load('4js接口-京东评论-评论数据.json')
    comments = comment_dict['comments']

    result_list = []
    for comment in comments:
        result_list.append({
            'id': comment['id'],
            'content': comment['content'],
            'creation_time': comment['creationTime'],
            'score': comment['score'],
            'nickname': comment['nickname'],
            'product_color': comment['productColor'],
            'product_size': comment['productSize']
        })

    return result_list


def save_db(comments):
    """
    :param: comments: {list} [{'id':123123, 'content':'物美价廉东西不错', },{}]
    :return: affected_rows : {int} 成功写入的行数
    """
    connection = pymysql.connect(host='127.0.0.1', port=3306,
                                 user='root',
                                 password='123456',
                                 db='jd',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
                                 )
    affected_rows = 0  # 成功计数

    for comment in comments:  # 循环评论
        cursor = connection.cursor()  # 创建游标
        # 先判断一下是否已存储过
        sql1 = "select id from comment where comment_id=%s " % (comment['id'])
        cursor.execute(sql1)
        rs_set = cursor.fetchone()  # 有值返回{'id':23} 无值返回None
        if rs_set:
            print('这条评论已存在在数据库中')
            continue
        # 不存在的写入数据库
        # 写法一： 参数为列表或元组  占位符 %s
        # sql2 = """
        # insert into comment (comment_id, content, creation_time, score, nickname, product_color, product_size)
        # values (%s, %s, %s, %s, %s,   %s, %s,)
        # """
        # 注意不要在拼sql的时候通过python字符串格式化（% .formate f''）传参，应该cursor.execute(args=)传参。
        # cursor.execute(sql2, args=(comment['id'], comment['content'], ...))     # 参数为列表或元组

        # 写法二：参数为字典
        sql2 = """
        insert into comment (comment_id, content, creation_time, score, nickname, product_color, product_size)
         values (%(id)s, %(content)s, %(creation_time)s, %(score)s, %(nickname)s,   %(product_color)s, %(product_size)s)
        """
        affected_row = cursor.execute(sql2, args=comment)
        if affected_row:
            print('本条评论插入成功')
            affected_rows += affected_row

        # 写法三：批量插入，拼sql
        # 写法四：批量插入，用现成方法executemany
    connection.commit()
    return affected_rows


if __name__ == '__main__':
    product_id = 100000287113  # 先写死，固定为一个商品下的评论
    page_amount = 10  # 爬取总页数，注意不要传给get_comments()函数导致每次请求固定的一页
    page_size = 10  # 每页10条评论
    time_sleep = 2

    for page in range(0, page_amount):
        comments_list = get_comments(product_id, page, page_size)
        affected_rows = save_db(comments=comments_list)
        print(f'成功写入{affected_rows}')
        time.sleep(2)

    print('Done')
"""
报错：
1. id int默认4字节太短  应该bigint
2. content中有单引号导致拼出的sql错误，应该在cursor.excute
sql = 'insert into comment (comment_id, content) values (%s, %s);' % (111232, '物美价廉')
sql = 'insert into comment (comment_id, content) values ({}, {});'.format(111232, '这个商品'太好'了！')
'insert into comment (comment_id, content) values (111232, '这个商品'太好'了！');'导致报错
cursor.execute(sql)
所以参数应该在cursor.execute(sql, args=(111232, '这个商品'太好'了！'))
3. indent error 缩进错误。  怀疑sql三引号中有一个空格，换行后变为5个空格。
"""