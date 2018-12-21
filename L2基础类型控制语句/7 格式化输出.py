# 格式化输出

# 简单输出
print('你好小明')
print('你好小红')
print('你好小宇')

# 带变量的输出
# 更有灵活性，易于维护，好处参考excercise1-3
name = '小明'
print(name)

# 加号拼接字符串
pay = '8'
print('花费一共' + pay + '元')

# print 里用逗号打印多个变量
name = '小明'
score = '90'
print(name, score)
print('学生姓名: ' + '学生成绩: ' + str(score))

# 但是，变量较多,加号拼接字符串比较麻烦
name = '小明'
score = '90'
sex = 'male'
height = 180
weight = 70
address = '郑州市xx街道'
phone = '14684548'

# 所以，我们使用格式化输出字符串
# 方法一: '姓名%s，成绩%'   % (变量1，变量2)
# %s 是占位符，将要被变量填充
# %s 字符串，  %d整数， %f 浮点数
# c语言写法，并不推荐写法，但很多项目再用这种写法，要求认识
print('学生姓名%s，成绩%d' % (name,score))

# 方法二：.format()
# 优点:不用转型。使用自然.
# 重点
print('学生姓名{}，成绩{}'.format(name, score))
# 其它不常用
print('学生姓名{stu_name),成绩{stu_score}'.format(name, score))(format(stu_name='小明', stu_score = 90))
# 小数点精度
print('河南省面积{: . 2f}'.format(190.5832))

# 左对齐右对齐
print('{:^20}'.format('对齐'))
print('{:<20}'.format('对齐'))
print('{:>20}'.format('对齐'))

# print()输出后不换行
# print('1',end =',')        #光标就不会换行
# print('2')
# '12'

# (重点)f-string  py3.6加入
# 优点 变量插值更直观灵活，动态计算速度快。
name = '小明'
age = 13
print(f'学生姓名:{name}, 年龄:{age}')
# 学生姓名:小明, 年龄:13