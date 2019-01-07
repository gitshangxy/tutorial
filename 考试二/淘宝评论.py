import requests
import json
import jieba, pygal
import pymysql.cursors
from wordcloud import WordCloud

class TaoBao(object):
    def __init__(self):
        self.conn= None
        self.cursor = None

        with open('tb_comments_1.json', encoding='utf-8') as f:
            self.commentd = json.load(f)
    def comment(self):
        # 读取数据
        comments = self.commentd['rateDetail']['rateList']
        # print(comments)
        for commentd in comments:
            data = []
            data.append(commentd['id'])
            data.append(commentd['rateDate'])
            content = '无'
            if commentd["appendComment"]:
                content = commentd["appendComment"]["content"]
            data.append(content)
            data.append(commentd['auctionSku'])
            data.append(commentd['rateContent'])

            print(f'id:{data[0]}\nrate_date:{data[1]}\nappend_cntent{data[2]}\naction_sku{data[3]}\nrate_cntent{data[4]}')
            self.save_mysql(data[0], data[1], data[2], data[3], data[4])

    def connection(self):
        self.conn = pymysql.connect(host='127.0.0.1', port=3306,
                                     user='root',
                                     password='123456',
                                     db='taobao',
                                     charset='utf8mb4'
                                     )

        self.cursor = self.conn.cursor()  # 创建游标

    def save_mysql(self, *args):
        self.connection()
        # 先判断一下是否已存储过
        sql1 = "select id from comments where comment_id=%s " % (args[0])
        self.cursor.execute(sql1)
        rs_set = self.cursor.fetchone()  # 有值返回{'id':23} 无值返回None
        if rs_set:
            print('这条评论已存在在数据库中')
        # 存入数据库
        sql2 = """
        insert into comments (comment_id, rate_date, append_content, action_sku, rate_content) values ('%s','%s','%s','%s','%s')
        """ % (args[0],args[1],args[2],args[3],args[4])
        affected_row = self.cursor.execute(sql2)
        if affected_row:
            print('本条评论插入成功')
        self.close()

    def close(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def get_comments(self):
        self.connection()
        sql1 = """ SELECT rate_content, append_content FROM comments; """
        self.cursor.execute(sql1)
        rs_set = self.cursor.fetchall()
        # print(rs_set)
        # self.close()
        # 分词
        list1 = ''
        for i in rs_set:
            list1 += i[0]+i[1]
        print(r'--'+list1)
        # 文字 生成词云
        font = 'msyh.ttc'
        wc = WordCloud(font_path=font,
                       background_color='white',
                       width=1000,
                       height=1000,
                       max_font_size=200,
                       min_font_size=50,
                       ).generate(list1)
        wc.to_file('淘宝评论.png')

        # 写成饼状图,读取手机的每个颜色
        self.cursor.execute(
            """select COUNT(action_sku) from comments WHERE action_sku = '网络类型:4G+全网通;机身颜色:金色;套餐类型:官方标配;存储容量:6+64GB'""")
        j = self.cursor.fetchone()
        self.cursor.execute(
            """select COUNT(action_sku) from comments WHERE action_sku = '网络类型:4G+全网通;机身颜色:黑色;套餐类型:官方标配;存储容量:6+64GB'""")
        h = self.cursor.fetchone()
        self.cursor.execute(
            """select COUNT(action_sku) from comments WHERE action_sku = '网络类型:4G+全网通;机身颜色:白色;套餐类型:官方标配;存储容量:6+64GB'""")
        b = self.cursor.fetchone()
        self.cursor.execute(
            """select COUNT(action_sku) from comments WHERE action_sku = '网络类型:4G+全网通;机身颜色:蓝色;套餐类型:官方标配;存储容量:6+64GB'""")
        l = self.cursor.fetchone()
        print(j, h, b, l)
        pie_chart = pygal.Pie()
        pie_chart.title = '根据action_sku分组，购买比例饼状图（in %)'
        pie_chart.add('金色', j[0] / 99)
        pie_chart.add('黑色', h[0] / 99)
        pie_chart.add('白色', b[0] / 99)
        pie_chart.add('蓝色', l[0] / 99)
        pie_chart.render_to_file('taobao.svg')
        self.close()

if __name__ =='__main__':
    content = TaoBao()
    content.comment()
    content.get_comments()
