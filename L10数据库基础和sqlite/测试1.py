import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

cursor.execute("""
   SELECT * FROM student3;
""")
student3s = cursor.fetchall()
print(student3s)

cursor.execute("""
   SELECT * FROM student3 WHERE age = '11';
""")

student3s = cursor.fetchall()
print(student3s)

cursor.execute("""
    UPDATE student3 SET age=22 where name = "小红"
""")
connect.commit()

# cursor.execute("""
#     DELETE FROM student3   where name = "小青", age=11;
# """)

# 假性删除，为了防止数据误删和方便找回。专门新建一个标识字段表示用户状态（正常、注销)
# cursor.update("""
#     UPDATE student3 SET del_flag=1 WHERE name="小红";
# """)
# connect.commit()
# cursor.execute("""
#     SELECT * FROM employee WHERE del_flag=0;
# """)


connect.close()
