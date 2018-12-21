# sqlite fetchall() 返回字典形式

"""
原[(1, '小明'),(2, '小红')]
需求[('id':1, 'name':'小明'),('id':2, 'name':'小红')]

百度后思路
1. 驱动方法https://www.jb51.net/article/94024.htm   cursor.description()
2. sql语句 http://www.hangge.com/blog/cache/detail_1454.html   PRAGMA table_info([employee]);
"""

import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

cursor.execute(""" select * from student3;""")
student3s = cursor.fetchall()
print(student3s)

print(cursor.description)
description = cursor.description
column_name_list = []
for i in description:
    column_name_list.append(i[0])     # 列名
print(column_name_list)

print('-'*50)
# 结果集拼成字典
result = []
for student3 in student3s:
    student3_dict = {}
    for index in range(0, len(column_name_list)):
        student3_dict[column_name_list[index]] = student3[index]
    print(student3_dict)
    result.append(student3_dict)

    # print(dict(zip(column_name_list, student3)))

print(result)

print('===')
print([dict(zip(column_name_list, student3)) for student3 in student3s])