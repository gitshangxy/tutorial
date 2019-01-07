# 综合项目：京东评论情感化分析
import jieba
import pymysql.cursors
from wordcloud import WordCloud

# 1. 从数据库把所有用户评论查出
def get_comments():
    # 连接数据库
    # 读表
    # select content from
    # return [{}, {}]

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='jd', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()  # 创建游标
    sql1 = """ SELECT content FROM comment; """
    cursor.execute(sql1)
    rs_set = cursor.fetchall()
    print(rs_set)

def process_comments():
    # 所有用户评论拼成一个长字符串
    return ''
    pass
def cut_word():
    #分词， 返回wordcloud包使用的格式
    # string ['手机', '好', '质量', '手机']
    results = jieba.cut('rs_set', cut_all=False)
    word_list = []
    for r in results:
        word_list.append(r)
    print(word_list)

    for r in results:
        print('生成器只能取一次', r)

def word_cloud(string):
    # 生成词云，保存到本地
    pass
    return None

def gen_pei():
    # 生成饼状图
    # select   count()   group by
    # 本地生成饼状图
    pass


if __name__ == '__main__':
     get_comments()


# 2. 所有用户评论拼成一个长字符串
# 3. 长字符串用jieba分词
# 4. 拼成wordcloud使用的结构，生成评论高频关键字词云。
# 5 pygal 根据用户productcolor 统计比例，查询pygal，饼状图文档

