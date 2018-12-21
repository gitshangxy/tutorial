# （了解）重载
# 面试题：重写跟重载的区别？
# 重写参考 L5/5类的继承2.py 一节

# 引题：写几个关于比大小的函数
# 1>给定两个数，返回最大的那个数
# 2>给定三个数，返回最大的那个数
# 3>传入数字组成的列表[1,0,-1,3.5]，返回最大的那项数字
# 1
def get_max1(num1, num2):
    max = num1
    if num2 > max:
        max = num2
        return max
print(get_max1(1,3))

# 2
def get_max2(num1, num2, num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num

    # if num2 > num1 and num2 > num3:
    #     max = num2
    # if num3 > num2 and num3 > num1:
    #     max = num3
    #     return max

print(get_max2(3,1,5))

# 3
def get_max3(list1):
    nummax = list1[0]
    # for i in list1:
    #     if i > nummax:
    #         nummax = i
    # return nummax
    for index, num in enumerate(list1):
        print(index, num)
        if num > nummax:
            nummax = num
    return nummax

print(get_max3(list1 = [1, 9, 3, -1]))



# N = int(input('输入需要对比大小数字的个数：'))
# print("请输入需要对比的数字：")
# num = []
# for i in range(1,N+1):
#     temp = int(input('输入第 %d 个数字' % i))
#     num.append (temp)
# print('您输入的数字为：',num)
# print('最大值为：',max(num))



# 2 把上面是三个函数封装到一个类中
# 3 然会觉得get_max1 get_max2看着难受，所以都变成get_max  python由于自身特性没有重载机制
class GetMaxNum(object):
    @staticmethod
    def get_max(num1, num2):
        if num2 > num1:
            return num2
        else:
            return num1

    @staticmethod
    def get_max(num1, num2, num3):
        max_num = num1
        if num2 > max_num:
            max_num = num2
        if num3 > max_num:
            max_num = num3
        return max_num

    @staticmethod
    def get_max(*list1):
        nummax = list1[0]
        for index, num in enumerate(list1):
            print(index, num)
            if num > nummax:
                nummax = num
        return nummax

# print('最大值',GetMaxNum.get_max1(1,3))
# print('最大值',GetMaxNum.get_max2(3,1,5))
# print('最大值',GetMaxNum.get_max3([1, 9, 3, -1]))

# GetMaxNum.get_max([3,1,5])        # 参类型可变
# GetMaxNum.get_max(3,1,5)
# GetMaxNum.get_max(True)

GetMaxNum.get_max(*[3,1,5])     # 参数个数可变

"""
重写：子类重写父类中的同名方法。
重载：类中有多个同名方法，参数个数不同，或参数类型不同，这种情况叫方法重载。针对方法参数的不同情况。
python当中没有重载机制，java语言中才有。同名函数重复定义，以最后为准。因为python是动态类型语言，传实参什么类型都接受：形参和实参可以传可变个数的参数。
"""