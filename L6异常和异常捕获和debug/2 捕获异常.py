# 捕获异常
# 场景：一个大型项目，业务逻辑复杂。当出现异常错误时，我们并不希望程序终止，希望程序主体功能运行；收集分析错误信息

# 示例1 捕获异常
def foo():
    try:
        print(1/0)
    except ZeroDivisionError:
        print('不能除以0')
    finally:
        print('我最后执行')
    print('world')
def boo():
    print('hello')
    foo()
    print('world')
boo()
"""
(重点)捕获异常： try..except..finally
try 括住可能发生问题的语句。偷懒方法try括住程序最外层，但这样捕获后不好定位出错的地方。
except ：后面跟异常的类名，如果捕获到这种异常，那么就会执行语句块，执行发生异常后的一些处理，处理比如 用户提示信息、记录日志、业务逻辑。
finally：不管程序正常运行，或是出现某种异常被捕获，在或是出现异常没有被捕获，最终都会执行
捕获异常应该适当使用，使用过多代码会乱，不用的话错误可能导致程序崩溃带来损失。 场景：捕获数据库操作代码。

"""

# 示例2
# f = open('demo.txt')
try:
    f = open('demo.txt')
    content = f.read()
    print(content)          # try块里面的变量变成局部变量，注意外部不用引用内部局部变量
except FileNotFoundError:
    print('文件未找到，请检查文件名')
except UnicodeDecodeError:
    print('unicode解码错误')
except Exception as e:  # e = FileNotFoundError()
    print(e)
finally:
    f.close()

"""
try块里面的变量变成局部变量，注意外部不用引用内部局部变量

如果try块中的代码可能报多种异常，那么多写几个并列的except 语句。

不知道错误类的类名：可能会出现代码中定义错误之外的未知新错误.使用所有错误类的父类Exception 类来捕获。
finally 场景：打开文件资源，不管有没有出错，最终应该保证关闭文件。

as 把...作为... 。关键字：类似等号赋值，可以写成一行
"""




