# 作业1
# 题二

f = [0,1,2,3,4,5,6]
new_list = []
def fn2(f):
    for i in range(0,len(f)):
        if i % 2 == 1:      # 奇数
            print(f[i])
            new_list.append(f[i])
    return new_list

print(fn2(f))




stuInfos = []
# 全局变量
newName = ""
newSex = ""
newPhone = ""


# 打印功能提示
def printMenu():
    print("=" * 30)
    print("      学生管理系统v1.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询学生信息")
    print("5.显示所有学生信息")
    print("0.退出系统")
    print("=" * 30)


# 获取一个学生的信息
def getInfo():
    global newName
    global newSex
    global newPhone
    # 这三个是全局变量，要对其进行修改，则要先声明
    newName = input("请输入学生的姓名：")
    newSex = input("请输入学生的性别：")
    newPhone = input("请输入学生的手机号码：")
    # 通过列表的形式把数据整合成一个整体，然后返回
    return [newName, newSex, newPhone]


# 添加学生信息
def addStuInfo():
    result = getInfo()
    newInfo = {}
    newInfo['name'] = result[0]
    newInfo['sex'] = result[1]
    newInfo['phone'] = result[2]
    stuInfos.append(newInfo)


# 修改一个学生的信息
def modifyStuInfo():
    stuId = int(input("请输入要修改的学生的序号："))
    getInfo()
    # 先获得要修改的学生在stuInfos中的位置，即stuId-1，当前位置是以字典形式存的，再找字典中要修改的值对应的键，即姓名···
    stuInfos[stuId - 1]['name'] = newName
    stuInfos[stuId - 1]['sex'] = newSex
    stuInfos[stuId - 1]['phone'] = newPhone


def main():
    while True:
        # 打印提示信息
        printMenu()
        key = input("请输入你要选择的操作：")
        if key == '1':
            # 添加学生信息
            addStuInfo()
        elif key == '3':
            # 修改学生信息
            modifyStuInfo()
        elif key == '5':
            print("=" * 30)
            print("学生的信息如下：")
            print("序号  姓名   性别   手机号码")
            i = 1
            for tempInfo in stuInfos:
                print("%d   %s   %s     %s" % (i, tempInfo['name'], tempInfo['sex'], tempInfo['phone']))
                i += 1


# 调用主函数
main()
