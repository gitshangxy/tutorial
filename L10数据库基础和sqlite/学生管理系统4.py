import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

# cursor.execute("""CREATE TABLE student5(
#                       id   INTEGER PRIMARY KEY AUTOINCREMENT,
#                       name TEXT,
#                       sex  VARCHAR(10),
#                       age  INTEGER,
#                       phone  TEXT
#         );""")

# 查询
def create_student5():
    cursor.execute(""" 
        SELECT * FROM student5;
    """)
    students_list = cursor.fetchall()
    print(students_list)

# 添加
def add_student5():
    print(create_student5())

    a = int(input("请输入要插入id号："))
    b = input("请输入要插入的学生姓名：")
    c = input("请输入要插入的学生性别：")
    d = input("请输入要插入的学生年龄：")
    e = int(input("请输入要插入的学生电话号码："))
    cursor.execute("""INSERT INTO student5(id,name,sex,age,phone) VALUES ('{}','{}','{}','{}','{}');
    """.format(a, b, c, d, e))
    cursor.execute(""" 
        SELECT * FROM student5;
        """)
    students = cursor.fetchall()
    print(students)


# 修改
def update_student5():
    pass
# 删除
def delete_student5():
    pass



def main():
    while True:
        print("""
        1-查询学员姓名')
        2-添加学员姓名')
        3-修改学员姓名')
        4-删除学员姓名')
        0-退出程序')
        """)

        num = int(input('请输入操作编码：'))

        if num == 1:
            create_student5()
        elif num == 2:
            add_student5()
        elif num == 3:
            update_student5()
        elif num == 4:
            delete_student5()
        elif num == 0:
            break


if __name__=='__main__' :
    main()

cursor.close()
connect.commit()
connect.close()
