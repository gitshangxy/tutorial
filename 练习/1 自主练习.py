# 去重
# a = {1,2,3,4,5,1,3}
# new_list = []
# for i in a:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# for x in [1,2,3,4]:
#     print('****')

# for i in range(1,11):
#     for j in range(1,i + 1):
#         print('*',end='')
#     print()

# for x in range(1,10):
#     for y in range(1,x+1):
#         print(y,end='')
#     print()

# 加 1--100
# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)

# 阶乘
# 方法一
# total = 1
# for i in range(1,11):
#     total = total * i
# print(total)
# 方法二  递归
# def fact(i):
#     if i == 1:
#         return i
#     return i * fact(i-1)
# print(fact(10))

# 输出奇数
# for num in range(1,101):
#     if num % 2 == 1:
#         print(num)





# list1 = []
# for i in range(1,10):
#     list1.append(i)
# print(list1)

# print([i for i in range(1,21)])

# list1 = "0123456789"
# list2 = ''
# for order, ch in enumerate(list1):
#     list2 += ch
#     if order % 2:
#         list2 += ' '
#     print(list2)


# list1='010609162526'
# import textwrap
# print(' '.join(textwrap.wrap(list1, width=2)))







# def sum(i):
#     if i == 1:
#         return 1
#     return sum(i-1)*i
# print(sum(5))


# total = 0
# for i in range(1, 101):
#     total = total + i
# print(total)


# def total(i):
#     if i == 1:
#         return 1
#     return total(i - 1) * i
# print(total(5))


# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return f(n-1)+f(n-2)
# for sum1 in range(1, 11):
#     print(f(sum1), ',', end='')

# i = 1000
# while i > 1:
#     i =i/2
#     print('h')
#     if i < 1:
#         break


# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))



