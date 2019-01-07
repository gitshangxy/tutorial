import csv
import json
import time
import requests
import pymysql.cursors


class JD_Comments(object):
    def __init__(self):
        self.base_url = 'https://sclub.jd.com/comment/productPageComments.action'
        self.headers = {
            'cookie': '__jdv=122270672|direct|-|none|-|1545816689735; __jdu=1911103525; PCSYCityID=412; shshshfpa=e81ca139-57b3-859d-db27-78339be22811-1545816702; user-key=e6e7b3db-b81e-4e29-8d18-2963aff81485; _pst=jd_598308d66b7f6; unick=jd_598308d66b7f6; pin=jd_598308d66b7f6; _tp=dS86tAtyZt57yHlL9R%2BNUu3v8O%2FrLAQD41K6mOOZVgg%3D; pinId=xwE-ZhW4nJSRvUbV4pUlxLV9-x-f3wj7; ipLoc-djd=1-72-2799-0; shshshfpb=hxt36K8P20YPw1TZmBAjdqQ%3D%3D; __jdc=122270672; cn=0; _gcl_au=1.1.1347703983.1545965749; 3AB9D23F7A4B3C9B=27LQVPUGGIYY62HSTBF7XSFP52OJPDLZZTFE2V3JLCCXY3FB2YGYEQRS62LZGQGPYS5HQLYJ4KMIM3UX2YXLVIDQBI; __jda=122270672.1911103525.1539428691.1545990246.1545996033.13; wlfstk_smdl=kzm0o495p17lw0iroflp4ztxhw8vfnf0; TrackID=1kVg6wrzKIkbIwtyAeS3byevhpy4PYoHZmtjXyALQiylRGYJOrvzo3iN5dZovKhbJ37a6iy5tOykVb7W7XNtTjM7FY7_zEQJ0sMnxvQI3BPA; ceshi3.com=000; shshshfp=447bcde9e37449b49000397db3ec679a; JSESSIONID=25722BAEFFFD84A72C0D98F183399A52.s1; shshshsID=94e5d0e01ba94413e0a2966cc1749b5c_10_1545997219070; __jdb=122270672.11.1911103525|13.1545996033; thor=480285E8F578B86999D37FE49A7A1F4E2ADA8E07A4BAB2F00C5E718B96CA586F9CCC3DAE4651567C4DEED22DB2E5E3E5F5638EAF8F42B2A74B54C1D995CA334B50838AA0D55C4146252ED75AE629497C8FE95F957CD05A75488DAE4679BD13A58DF869E5C8288ACFD091CFE7A6F02E38924B53AA6844C9BA3E665876FFD05AA75BEFEDBA779B1945DE5D5A2A76DF8CF9F1BC2D46DBC84ABD1799F41D5E0511A7',
            'referer': 'https://item.jd.com/100000287113.html',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }
        self.page_num = 0
        self.html = ''
        self.retry = 0
        self.count = 0
        self.coon = None
        self.cursor = None
        self.save_header_csv()

    def connection(self):
        self.coon = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='123456',
            db='jd',
            charset='utf8mb4'
        )
        self.cursor = self.coon.cursor()

    def close_sql(self):
        self.coon.commit()
        self.cursor.close()
        self.coon.close()

    def get_html(self, url, params):
        """
        对商品评论发请求
        :return:
        """
        try:
            self.retry += 1
            response = requests.get(url, params=params, headers=self.headers)
            self.html = response.text
            # print(self.html)
        except Exception as e:
            if self.retry > 3:
                print(f'请求失败，正在尝试第{self.retry}次重新请求')
                time.sleep(3)
                return
            self.get_html(self.base_url, params)
        else:
            self.retry = 0
        finally:
            self.page_num += 1

    def parse(self):
        """
        获取json数据，转成字典，得到想要的数据
        :return:
        """
        data_list = []
        comment_json = json.loads(self.html)
        comments = comment_json["comments"]
        for c in comments:
            datas = []
            # 保存到列表中
            datas.append(c["nickname"])
            datas.append(c["userLevelName"])
            datas.append(c["referenceName"])
            datas.append(c["content"].replace('\n', '').replace('\r', '').strip())
            datas.append(c["creationTime"])
            datas.append(c["score"])
            datas.append(c["productSize"])
            datas.append(c["productColor"])
            datas.append(c["replyCount"])
            datas.append(c["usefulVoteCount"])
            data_list.append(datas)
            # print(data_list)
            self.save_mysql(datas[0], datas[1], datas[2], datas[3], datas[4], datas[5], datas[6], datas[7], datas[8], datas[9])
        self.save_data_csv(data_list)
        print('第{}页数据爬取完毕，等待数据保存'.format(self.page_num))
        time.sleep(3)

    def save_mysql(self, *args):
        """
        保存到mysql数据库
        :return:
        """
        self.connection()
        try:
            with self.cursor as cursor:
                sql = """INSERT INTO jd_comment (nickname, user_level, phone_message, content, create_time, score, pro_size, color, reply_num, useful_num) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {}, {})""".format(args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7], args[8], args[9])
                cursor.execute(sql)
        except Exception as e:
            print(e)
        finally:
            self.close_sql()

    def save_header_csv(self):
        headers = [['用户名', '会员等级', '商品信息', '评论内容', '评论时间', '评分', '版本', '颜色', '回复数', '点赞数']]
        with open('京东评论.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(headers)

    def save_data_csv(self, data_list):
        with open('京东评论.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data_list)

    def run(self):
        while True:
            params = {
                'productId': 5089253,
                'sortType': 5,
                'score': 0,
                'page': self.page_num,
                'pageSize': 10,
            }
            self.get_html(self.base_url, params)
            self.parse()
            if self.page_num == 10:
                break


if __name__ == '__main__':
    jdc = JD_Comments()
    jdc.run()



