# 学生管理系统-v2  字典
# tip:pycharm左侧的structure可以看脚本结构。

students = [{'name': '小明', 'age': 10, 'sex': 'male'},
            {'name': '小红', 'age': 12, 'sex': 'female'},
            {'name': '小李', 'age': 12, 'sex': 'male'}
            ]

def show_students():
    print('行号\t\t姓名\t\t年龄\t\t性别')
    print('------------------------------------------')

    for i in range(0, len(students)):
        stu_dict = students[i]      # {'name': '小红', 'age': 12, 'sex': 'female'}
        name =stu_dict['name']
        age = stu_dict['age']
        sex = stu_dict['sex']
        print('{:<12}{:<12}{:<12}{:<12}'.format(i+1, name, age, sex))

    # for i in range(1, len(students) + 1):
    #     name = students[i - 1]['name']
    #     age = students[i - 1]['age']
    #     sex = students[i - 1]['sex']
    #     print('{:<12}{:<12}{:<12}{:<12}'.format(i, name, age, sex))


def and_student():
    # 添加

    # add_new = {}
    add_name = input('输入添加学员姓名：')
    add_age = int(input('输入添加学员年龄：'))
    add_sex = input('输入添加学员性别：')
    add_new = {'name': add_name, 'age': add_age, 'sex': add_sex}
    students.append(add_new)
    print('添加成功')

def update_student():
    # 修改
    show_students()             #显示学生列表

    i = int(input('要修改第几个：'))
    students[i - 1]['name'] = input('修改后的学员姓名：')
    students[i-1]['age'] = int(input('修改后的年龄：'))
    print(students)
    print('修改成功')

def delete_student():
    # 删除
    print(""" 删除> 请输入子操作编号：
                              1)按学生编号删除
                              2)删除所有学生(谨慎)
                  """)
    sub_num = int(input('请选择子操作:'))
    if sub_num == 1:
        num_name = int(input('要删除第几个学员：'))
        students.pop(num_name - 1)
        print('删除成功')
    elif sub_num == 2:
        confirm = input('确定删除全部? (Y/N)')
        if confirm == 'Y' or confirm == 'y':
            students.clear()
            print('删除全部成功')

def main():
    # 主函数，程序入口
    while True:
        print("""
        1-查询学员姓名')
        2-添加学员姓名')
        3-修改学员姓名')
        4-删除学员姓名')
        0-退出程序')
        """)

        num = int(input('请输入操作编号: '))

        if num == 1:
            show_students()
        elif num == 2:
            and_student()
        elif num == 3:
            update_student()
        elif num == 4:
            delete_student()
        elif num == 0:
            break

# 调用主函数
# main()
if __name__=='__main__':    # 这种写法含义将会在‘包，模块’一节中讲
    main()
