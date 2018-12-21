student_list = ['小米', '小红', '小明']
while True:
    print('1.查询学员姓名')
    print('2.添加学员姓名')
    print('3.修改学员姓名')
    print('4.删除学员姓名')
    print('0.退出程序')

    num = int(input('请输入操作编号: '))

    if num == 1:        #打印学生列表
        print('行号\t\t姓名')
        print('------------------')
        for stu in range(0, len(student_list)):
            print(stu+1, ' \t\t ', student_list[stu])

    elif num == 2:
        #添加
        i = input('输入添加学员姓名：')
        student_list.append(i)
        print('添加成功')

    elif num == 3:
        # 修改
        print('行号\t\t姓名')
        print('------------------')
        for i in range(0, len(student_list)):
            print(i+1, '\t\t', student_list[i])

        stu_num = int(input('要修改第几个：'))
        student_list[stu_num-1] = input('修改后的学员姓名：')
        print('修改成功')

    elif num == 4:
        # 删除
        print(""" 删除> 请输入子操作编号：
                    1)按学生编号删除
                    2)删除所有学生(谨慎)
        """)
        sub_num = int(input('请选择子操作:'))
        if sub_num == 1:
            s = int(input('要删除第几个学员：'))
            student_list.pop(s - 1)
            print('删除成功')
        elif sub_num == 2:
            confirm = input('确定删除全部? (Y/N)')
            if confirm == 'Y' or  confirm == 'y':
                student_list.clear()
                print('删除全部成功')

    elif num == 0:
        print('谢谢使用')
        break












