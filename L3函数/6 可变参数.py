# （了解）可变参数（讲完列表字典后江）

# 引题：有些函数的参数比较多，都写出来比较长不方便写和看；传实参的个数不确定。
def print_stu_info(name='',age='',sex='',score='',address='',phone=0):
    pass
def get_max_num(a,b,c,d,e,f,g):
    pass

# 上面的参数a,b,c,d,e,f,g结构有点像列表，所以 python 就提供一种方便表示不固定数量参数的语法。
# 可变列表参数： 起一个形参名来接收列表 多个参数组成列表。为了标识这个参数是特别的，前面有个*号。
def print_stu_info(*args):          # '小明', '小红'
    print(args)
    for i in args:
        print(i)
    # 拿到参数后在函数体内继续进行运算。

print_stu_info(* ['小明', '小红', '小李', '小青'])

# 这个例子只传入了一个参数，参数类型为列表。上面的例子传入的是不同方面的参数，只不过用列表把他们装在了一起本质是传入多个参数。
def print_stu_info4(l):
    for i in l:
        print(i)
print_stu_info(l=['小明', '小红', '小李', '小青'])

# 可变字典参数
def print_stu_info2(**kwargs):
    print(kwargs)
    print(kwargs['name'])
    print(kwargs['age'])

print_stu_info(**{'name':'小明', 'age':10, 'sex':'male', 'score':90})
# 可变参数好处： 参数数量可变，修改方便，代码量比较少。逻辑都在函数中，代码整体可读性好。

# 可变参数的位置。字典参数必须要在列表参数之后
def print_stu_info3(a, b=0, *args, **kwargs):
    pass
print_stu_info3()


# 面试：函数中有哪几种参数？顺序有没有要求？

