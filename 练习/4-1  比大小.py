# 1
# a = int(input('输出第一个数:'))
# b = int(input('输出第二个数:'))
# c = int(input('输出第三个数:'))
# max_num = a         #存储最大值
# if a >= b >= c or a >= c >= b:
#     print('第一个数大')
# elif b >= a >= c or b >= c >= a:
#     print('第二个数大')
# else:
#     print('第三个数大')

#2函数

a = int(input('一:'))
b = int(input('二:'))
c = int(input('三:'))
max = a
if a > b:
    max = a
    if a > c:
        max = a
    else:
        max = c
elif b > a:
    if b > c:
        max = b
    else:
        max = c
print(max)

# 3

# a = int(input('一:'))
# b = int(input('二:'))
# c = int(input('三:'))
# max_num  = a
#
# if b > max_num:
#     max_num = b
# if c > max_num:
#     max_num = c
#
# print('最大值',max_num)



