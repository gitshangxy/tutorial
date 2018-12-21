# 作用域
# 作用域：

# 1,块级作用域
# 外调内（不推荐）
# if 1==1:
#     name = '小明'
#     print(name)
# print(name)
#
# for i in range(10):
#     age = i
# print(age)

# 内调外
# total = 0
# for i in range(1, 10):
#     total += i
# print(total)



# 在语句块中声明变量，最好在同一级下进行操作，如果在语句块外引用变量，python并不会报错。但是在其他iava/c++是会报错的。
# （不推荐） 外层访问内层声明的变量。
# 外层先声明，内层在访问：  if   for 语句块都可以调用外层声明过的变量，同一级代码可以访问同一级之间声明过的变量。

## 2 局部作用域

# def foo():
#     name = '小明'
#     if 1==1:
#         print(name)
#
# def boo():
#     ame2 = 'xxx'
#     age = 13
#
# print(ccc)
# print(name)

# 外部变量：函数之外的变量。
# 局部变量local variable：函数内定义变量。
# 局部变量作用域：声明这个局部变量的函数内。 不同函数之间互相调用各自的局部变量。不同函数的变量相互隔离。
# 可能出错的地方： 外部直接调用内部变量会报错NameError: name 'name' is not defined

# 3 作用域链
name = '小明'
def f1():
    name = '小李'

    def f2():
        name = '小红'
        print(name)
    f2()
f1()
# 作用于嵌套：例如上例 全局套着函数，函数1 套着函数2。调用变量时会现在当前函数作用域中查找，如果找不到的话会去上一级函数的作用域中查找。 当前层< 父层< 最外层全局。
# 平时代码应该避免函数复杂嵌套，变量作用域把握不准时生命不同名字的变量。


# 练习
name = '小明'

def f1():
    print(name)

def f2():
    name = '小红'
    f1()

f1()

# 4 内置作用域
# 在上面的例子中 ，你可以在任何地方使用print type abs 一些函数，函数其实是一个指向功能的变量。这些函数的作用域是内置作用域。

# 作用域范围从小到大：内存局部< 外层局部< 全局< 内置全局
