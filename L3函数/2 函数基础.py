# 函数基础
# 函数 function 将重复公共的代码抽象出来，多次调用。封装代码，函数把业务逻辑打包起来我们使用时直接调用，不必关心内部是如何实现的，降低项目的实现难度。实现某一种功能。好处：减少重复代码节省代码量；模块逻辑清晰。
def calculate_area(r):
    print('圆面积',3.14 * r * r)

calculate_area(10)
calculate_area(3)
calculate_area(5)

# 语法
## 函数定义：关键字 def(define) 函数名（参数）：   语句块
## 参数：函数运行前需要告诉函数一些运行时需要的信息原料、数值，函数根据传入的参数，参与内部的逻辑运算。
## 函数调用：函数名（参数）