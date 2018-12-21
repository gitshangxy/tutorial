



















#
# import MySQLdb
# db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
# cursor = db.cursor(MySQLdb.cursors.DictCursor)
# results = cursor.fetchall()


# -*- coding: utf-8 -*-
import sqlite3

# 连接数据库
con = sqlite3.connect("testsqlite.db")
cur = con.cursor()


# 查询记录总数
cur.execute("""
    SELECT id, name FROM student;
""")

# total = cur.fetchone()
#
# # 返回元组类型
# print(total)


rows = cur.fetchall()

for row in rows:
    print (row)