# 学生管理4 sqlite版
import sqlite3

def create_table():
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE students
        (
            id integer PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            sex TEXT,
            age INTEGER,
            phone TEXT
        );
    """)
    connect.commit()
    cursor.close()
    connect.close()

def show_students():
    """
    展示学生列表
    """

    print('行号\t\t姓名\t\t性别\t\t年龄\t\t电话')
    print('---------------------------------------------------')
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    cursor.execute("""
        SELECT * FROM students;
    """)
    students_list = cursor.fetchall()    # [(1,小明), ()]
    for index, student in enumerate(students_list):
        print(f'{index+1}\t\t\t{student[1]}\t\t{student[2]}\t\t\t{student[3]}\t\t{student[4]}')
        # cursor.close()
        # connect.close()

# 添加
def add_students():

    show_students()

    name = input("新的学生姓名：")
    sex = input("新的学生性别：")
    age = input("新的学生年龄：")
    phone = int(input("新的学生电话："))

    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    # sql = """
    # INSERT INTO students(name, sex, age, phone) VALUES ("%s", "%s","%s" , "%s");
    #     """ % (name, sex, age, phone)
    sql = f"""
        insert into students(name, sex, age, phone) values ("{name}", "{sex}", "{age}", "{phone}");
    """

    print(sql)
    cursor.execute(sql)
    connect.commit()
    connect.close()
    print('添加成功')

# 修改
def update_students():
    # 数据库的设计 应该多一列 学生编号。 id列面向数据库为了安全不适合向用户展示。
    show_students()

    id = int(input('要修改id号：'))
    new_name = input('输入新名字')
    new_sex = input('输入新性别')
    new_age = input('输入新年龄')
    new_phone = input('输入新电话')
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    # 先查询输入的学生是否存在，存在的话更新，不存在的给出用户提示
    sql2 = f"""
        SELECT 1 FROM students WHERE id={id};
    """
    cursor.execute(sql2)
    student = cursor.fetchall()
    if student:
        sql2 = f"""
            UPDATE students SET name="{new_name}", sex="{new_sex}", age="{new_age}", phone="{new_phone}" WHERE id={id};
        """

        cursor.execute(sql2)
        connect.commit()
        print('修改成功')
    else:
        print('学生id不存在，请重新存在。')
    connect.close()

# 删除
def delete_students():

    show_students()
    print(""" 删除> 请输入子操作编号：
                                  1)按id号删除,删除某一行
                                  2)删除整张表的内容(谨慎)
                                  3)删除整张表(谨慎)
                      """)
    sub_num = int(input('请选择子操作:'))
    if sub_num == 1:
        connect = sqlite3.connect("testsqlite.db")
        cursor = connect.cursor()
        num_name = int(input('要删除id为几的学员：'))
        s1 = f"""
            DELETE FROM students WHERE id={num_name};
        """
        cursor.execute(s1)
        connect.commit()
        connect.close()
        print('删除成功')

    elif sub_num == 2:
        confirm = input('确定删除全部? (Y/N)')
        if confirm == 'Y' or confirm == 'y':
            connect = sqlite3.connect("testsqlite.db")
            cursor = connect.cursor()
            s2 = f"""
                DELETE FROM students;
            """
            cursor.execute(s2)
            connect.commit()
            connect.close()
            print('删除表内容成功')

    elif sub_num == 3:
        confirm2 = input('确定删除全部? (Y/N)')
        if confirm2 == 'Y' or confirm2 == 'y':
            connect = sqlite3.connect("testsqlite.db")
            cursor = connect.cursor()
            s3 = f"""
                drop table students;
            """
            cursor.execute(s3)
            connect.commit()
            connect.close()
            print('删除表内容成功')


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
            show_students()
        elif num == 2:
            add_students()
        elif num == 3:
            update_students()
        elif num == 4:
            delete_students()
        elif num == 0:
            break


if __name__=='__main__' :
    main()



# ke可能出现的错误：
# 插入功能
# sql = """
#     INSERT INTO students(name, sex, age, phone) VALUES (%s, {%s, %d, %d);
#         """ % (name, sex, age, phone)