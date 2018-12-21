students = [{'name': '小明','age': 10,'sex':'male'},
            {'name': '小红','age': 12,'sex':'female'},
            {'name': '小李','age': 12,'sex':'male'}
            ]

while True:
    print("""1)查询学员姓名
            2）添加学员姓名
            3）修改学员姓名
            4）删除学员姓名
            0）退出程序""")
    num = int(input('请输入操作编号: '))
    if num == 1:
        print('行号\t\t姓名\t\t年龄\t\t性别')
        print('------------------------------------------')
    for i in range(1, len(students)+1):
        name = students[i-1]['name']
        age = students[i-1]['age']
        sex = students[i-1]['sex']
        print('{:<12}{:<12}{:<12}{:<12}'.format(i, name, age, sex))


    if num == 2:
        # 添加
        add_new = {}

        add_name = input('输入添加学员姓名：')
        add_age = input('输入添加学员年龄：')
        add_sex = input('输入添加学员性别：')
        add_new = {'name':add_name, 'age':add_age, 'sex':add_sex}
        students.append(add_new)
        print('添加成功')

    if num == 3:
        # 修改
        # print('行号\t\t姓名\t\t年龄\t\t性别')
        # print('------------------------------------------')
        # for i in range(1, len(students) + 1):
        #     name = students[i - 1]['name']
        #     age = students[i - 1]['age']
        #     sex = students[i - 1]['sex']
        #     print('{:<12}{:<12}{:<12}{:<12}'.format(i, name, age, sex))


        i = int(input('要修改第几个：'))
        students[i - 1]['name'] = input('修改后的学员姓名：')
        students[i-1]['age']= input('修改后的年龄：')

        print('修改成功')

    if num == 4:
        # 删除
        print(""" 删除> 请输入子操作编号：
                            1)按学生编号删除
                            2)删除所有学生(谨慎)
                """)
        sub_num = int(input('请选择子操作:'))
        if sub_num == 1:
            s = int(input('要删除第几个学员：'))
            students.pop(s - 1)
            print('删除成功')
        elif sub_num == 2:
            confirm = input('确定删除全部? (Y/N)')
            if confirm == 'Y' or confirm == 'y':
                students.clear()
                print('删除全部成功')
        pass
    if num == 0:
        print('谢谢使用')
        break


