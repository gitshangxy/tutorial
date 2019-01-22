# os
# os包：IOS macOS , operate system 操作系统。主要负责新建文件、改文件名、路径、操作电脑系统相关的功能。是一个内置包。os包实质调用的是windows上的编程接口

import os
# from os import path, open
# from os import *


# 1> os.path.exists  判断是否存在文件。 判断路径是否存在。
print(os.path.exists('1包引用.py'))    # True
print(os.path.exists('text.txt'))    # False
os.path.exists('D:\\pycharm尚小雨')

# 2> 重命名
# os.rename('aaa.txt', 'bbb.txt')

# 3> 删除文件
# os.remove('bbb.txt')

# 4> 创建文件夹  make directory
# os.mkdir('aaa')   # 只能创建单层路径
# os.makedirs('bbb/bb')   # 可以一次创建多层路径

# 5> 列出当前文件夹下的文件，相当于cmd中的dir命令 ,linux Is。
os.listdir()

# 6> 切换当前文件夹 change ,  相当于cmd中的cd命令
# os.chdir('aaa')

# 在cmd中尝试dir 、cd命令
# 7> 获取当前工作目录路径  get work directory
print(os.getcwd())
# 7> 获取当前文件所在文件夹。与os.getcwd()不一样的地方，getcwd会受os.chdir()。os.path.dirname只会返回当前文件的所在目录，路径分隔用正斜杠。__file__表示文件名、自身
print(os.path.dirname(__file__))

# 相对路径和绝对路径(针对资源管理器路径)
# 绝对路径：从盘符或项目根目录写出每一层目录层级到文件  D:\pycharm尚小雨\tutorial\L8包\3os.pty   优点是准确，缺点写起来麻烦。
# 相对路径:  .当前目录    ..表示父目录
# 相对3os.py而言，./1包引用.py    L8包/1包引用.py   ../L7本地文件读写/xx.py
# 相对路径的优点写起来比较短，整个文件夹路径变化时里面的文件路径不用修改。缺点是容易写错、没有绝对路径准确。
# 表示目录层级斜杠：Windows上 | 反斜杠， macOS linux 用的是/正斜杠。pycharm解释器会把字符串中的反斜杠认为是转义字符，导致出错。
# 解决方案：
# 1. 反斜杠变为正斜杠 'D:/pycharm尚小雨/tutorial/L8包/3os.pty'
# 2. 使用转义字符输出反斜杠 'D:\\pycharm尚小雨\\tutorial\\L8包\\3os.pty'

# 8> (常用) 拼接路径,获取脚本的绝对路径
print(os.path.join(os.getcwd(), '3os.py'))

# 9> 返回绝对路径   absolute
print(os.path.abspath('./1包引用.py'))
os.path.abspath(os.path.join(os.getcwd(), '3os.py'))

# 10> 判断是否路径
print(os.path.isdir('aaa'))

# linux系统上操作可能需要权限



## 作业1：使用绝对路径打开L7/chinese_utf8.txt

with open('D:/pycharm尚小雨/tutorial/L7本地文件读写/chinese_utf8.txt', 'r', encoding='utf-8')as f:
    content = f.read()
    print(content)

"""
作业二：
基础：选择资源管理器上的一个文件夹，批量重命名里面杂乱的文件，文件名  文件1,文件2,文件3。
追加1: 不同类型文件txt doc jpg 。
追加2：读取文件元信息，把创建时间 来重命名文件。
追加3：修改文件元信息
知识点：for循环 os.listdir  百度os包获取文件名后缀  split('.')
"""