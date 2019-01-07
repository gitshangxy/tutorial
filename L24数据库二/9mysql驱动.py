# mysql驱动
# 引题：已经学习了sql语法，sqlite驱动操作sqlite数据库，daragrip的 jdbc java驱动操作mysql。所以我们要找python操作mysql驱动
"""
驱动选择：
1. MySQLDB。 已经有C驱动mysql的成熟包，Mysqldb包python对这个c驱动包封装。优点是效率高，py2环境和众多项目中使用。
pip install mysql-connector
pip install PyMySQL
pip install MySQL-python
缺点windows下pip安装报错(因为pypi中压根没这个包)。可以去网上找对应平台编译后的.whl安装(也可能报错)。最终解决去mysql官方下载对应平台的connector.msi安装。
2. mysql-connector 。python书写，类似于MySQLdb但不依赖于c语言驱动
3. (推荐)pymysql。纯python写的。缺点效率稍低。 优点安装方便，完全兼容mysqldb的语法。市场占有越来越高。
"""

import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='root',
                             password='123456',  # 安全风险，未来会从环境变量读取
                             db='test',
                             charset='utf8mb4',  # 可以省略，8.0客户端默认utf-8可以省略，5.x最好带上
                             cursorclass=pymysql.cursors.DictCursor  # 返回字典格式的结果集。不写返回默认元祖格式。
                             )

try:
    # 查询
    with connection.cursor() as cursor:
        sql = """ SELECT * FROM shirt; """
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        for row in result:
            print('小红有一件{}色的{}'.format(row['color'], row['style']))

    # 添加
    # with connection.cursor() as cursor:
    #     sql = """ INSERT INTO shirt values (%s, %s, %s, %s) """
    #     affected_rows = cursor.execute(sql, (None, '裙子', '绿', 2))
    #     print(affected_rows)
    # connection.commit()

    # 修改  按主键
    # with connection.cursor() as cursor:
    #     sql = """ UPDATE shirt set color='黄' where id=5; """
    #     result = cursor.execute(sql)
    #     print(result)
    #     connection.commit()

    # 连接person修改shirt
    with connection.cursor() as cursor:
        sql = """ SELECT id FROM person WHERE name='小红'; """
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        xiaohong_id = result['id']
        print(xiaohong_id)
        sql = """ UPDATE shirt set color='黄' where person_id=%s and style='外套'; """
        cursor.execute(sql, (xiaohong_id))
        r = cursor.fetchall()
        print(r)
        connection.commit()
except Exception as e:
    print(e)
finally:
    connection.close()


# 扁平写法
# cursor = connection.cursor()
# cursor.exe()
# cursor.fetchall()
# cursor.close()
# connection.close()
