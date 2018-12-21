# (了解)PEP8代码风格指导

"""
PEP  python Enhancement Proposal, python相关功能官方声明。
PEP8  python增强方案第八号文件，这个文件说明了python 语言代码应该怎么书写，指导了书写风格。当你的代码没有做到文件要求的时候，python会报灰线轻度提示。没有完全遵守规则不影响代码执行，但建议遵守。
"""

#  操作符前面应该有一个空格
a = 3
a = 3


# 顶层方法与方法间有两个空行
def foo():
    pass


def boo():
    pass


# 类中的方法相隔一行
class Student(object):
    def foo(self):
        pass

    def boo(self):
        pass


# 类与类之间空两行
# 如果没有父类不写括号
# 类名应该用驼峰风格
class aaa():
    pass


class Bbb:
    pass


# 方法名、类名不要重复使用
def boo():
    pass


# 两个条件有时可以写成链式的
if 1 < a and a < 2:
    pass
if 1 < a < 2:
    pass

# 不建议代码写的过长，80个字符。pycharm的提示灰线在120个字符。
# 是大法官就让他意识到法国红酒法通过五色入狱is对方提供用户为儿童一个人提供合适的而非通过人的各色人垫付色的人分通过而地

# 文件末尾代码时另起一新行
print('end')
# 字典冒号后空格 括号
print({'name': '小明', 'age': 13})

"""
pycharm有关代码风格操作
1. 界面右下角图标点击，调节提示出现的级别（不提示、语法、拼写）。
2. 自动格式化代码快捷工具，界面左上菜单 code/reformat code 。
"""

"""
参考文章
PEP8编程规范
(英文)https://www.python.org/dev/peps/pep-0008/
(中文)https://blog.csdn.net/ratsniper/article/details/78954852

"""
