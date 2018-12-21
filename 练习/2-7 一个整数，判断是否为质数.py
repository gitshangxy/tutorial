# 7提示  定义一个变量记录可以整除的次数
# 10 % 2 == 0
#
# 19 % 1 == 0
# ,,,,,
# 19 % 19 == 0
# 整除次数>2合数    =2质数

num = 15
total = 0

if num == 1:
    print('1既不是质数也不是合数')

for i in range(1, num+1):
    if num % i == 0:
        total = total + 1

#能被1和自身整除
if total == 2:
    print(num, '质数')
#能被1，自身，和其它数整除
elif total > 2:
    print(num, '合数')




