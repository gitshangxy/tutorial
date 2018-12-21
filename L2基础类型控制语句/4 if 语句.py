# 主题： 控制语句之if
# 多行注释  ctel+/    或  shift+冒号

# age = 10
# if age > 18:
#     print('年龄大于18是成人')
# else:
#     print('未成年')
#
# score = 'hello'
# if score < 0 or score > 100:
#     print('分数不合法')
# elif score < 60:
#     print ('不及格')
# elif 60 <score > 70:
#     print('及格')
# elif 70 <= score and score < 90:
#     print('良')
# elif score >= 90:
#     print('优秀')
# else:
#     print('请输出整数')


# if<条件> ：
#  条件为true或（非空的字符串，非空的列表）后执行的语句 关键字if判断条件，为true执行代码块中的语句，False的时候不执行。

# if<条件1>:   条件1为True  执行语句   else  不满足上面条件的时候执行的语句
"""更多的选择分支
if <条件1>：
    ...
elif<条件2>：
    ...
elif<条件3>:
    ...
...从上到下判断各个条件，如果走入一个分支，其它分支再走。设计项目需要注意。还要注意 if 控制语句的嵌套层数不要超过四层

pass:不执行实际功能，只是为了占位置

"""

# 表达式： 一句代码。
# 语句块： 后面的代码是从属于前面的一个语句。语句特点：一条语句，然后有一个冒号，然后语句块以缩进（4 个空格或一个tab）开始，语句块具有明显的层级关系。其它语句靠{}和; 来区分语句块

# 缩进：python要求语句块强制缩进。必须为4个空格。tab和shift+tab调整代码缩进。
# 缩进错误会报错'IndentationError: unexpected indent'

# (语法糖)：if语句单行写法
def get_max1(num1,num2):
    # if num1 > num2:
    #     return num1
    # else:
    #     return num2
    return num1 if num1 > num2 else num2
print(get_max1(1,4))
print(get_max1(4,1))
# 类似三元表达式c=a>b?1:0
# if else语句块写成单行模式     return 返回值1  if 条件 else 返回值2, 当if 条件为True返回返回值1， 为False返回返回值2.

"""地地道道的 
地地道道的
地地道道的
"""