nterms = int(input("你需要几项？"))

# 第一和第二项
n1 = 1
n2 = 1
count = 2

# 判断输入的值是否合法
if nterms <= 1:
    print("请输入一个正整数。")
elif nterms == 1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1, ",", n2, end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth, end=" , ")
        # 更新值
        n1 = n2
        n2 = nth
        count += 1

# a 代表前第二个数
# b代表前第一个数
# c代表前两个数的和
print('1、''1、',end='')
a = 1
b = 1

for i in range(3,10):
    c = a + b
    print(c,'、',end='')
    a = b
    b = c


