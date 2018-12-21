# 1 计算两个数的乘积

def fact(sum1,sum2):
    return sum1 * sum2
print(fact(2, 3))


# 2 圆

def yuan(r):
    a=3.14*r*r
    print(a)
yuan(2)
def zheng(b):
    t=b*b*b
    print(t)
zheng(3)
def qiu(y):
    i=(3/4)*3.14*y*y*y
    print(i)
qiu(3)


# 3 输入成绩， 判断评分

def sum1(score):
    if 90 <= score <= 100:
        print("等级为A")
    elif 80 <= score <= 89:
        print("等级为B")
    elif 70 <= score <= 79:
        print("等级为C")
    elif 60 <= score <= 69:
        print("等级为D")
    elif 0 <= score < 60:
        print("等级为F")
    else:
        print('输入不合法')
sum1(89)


# 4 接收用户输入的年份，判断年份是否为闰年

def year():
    num_year = int(input('请输入一个年份：'))
    if num_year % 4 == 0 and not num_year % 100 == 0 or num_year % 400 == 0:
        print("该年份为闰年")
    else:
        print('该年份为平年')
year()


# 5 计算1+2+3...+49 的和
def total(s):
    if s == 1:
        return 1
    return total(s - 1) + s
print(total(49))


# 6 公约数
def hcf(x, y):
    if x > y:
        smaller = x
    else:
        smaller = y

    for i in range(1,smaller + 1):
        if ((x % i == 0)and(y % i == 0)):
            hcf = i
    return hcf
num1 = int(input('请输入第一个数字：'))
num2 = int(input('请输入第二个数字：'))
print(num1,'和',num2,'的最大公约数为',hcf(num1,num2))


# 7 去重

list1 = [1, 2, 3, 2, 1, 4, 5]
new_list = []
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)


# 8 已知列表，求最大值
list1 = [2, -1, 5, 0, 99, -1]

def get_max1(list1):
    nummax = list1[0]
    for i in list1:
        if i > nummax:
            nummax = i
    return nummax

print(get_max1(list1))


# 9 手机类

class Phone():
    def __init__(self, brand, price, stock):
        self.brand = brand
        self.price = price
        self.stock = stock

    def print_info(self):
        print('手机品牌{},价格{},库存数量{}'.format(self.brand,self. price,self.stock))

num1 = Phone('华为', 3400, 1000)
num2 = Phone('小明', 3000, 900)

num1.print_info()
num2.print_info()
