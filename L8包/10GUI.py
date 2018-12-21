# （了解）GUI
# GUI: graphic User Interface, 图形用户界面。我们平时用的qq、python、搜狗输入法工具栏这些软件的界面都叫GUI开发。因为GUI相关库不生态统一、学习成本、功能、盈利等方面问起，目前开发者不多。
# windows上的软件图形界面底层调用是C++ directX 底层图形接口。其他语言的开发者封装win底层图形接口形成自己语言可以调用的图形库。例如 iava中的AWT swing, python中的 TKinter GTk wxwidgets qt5。有兴趣的话可以深入学习GUI领域。

from tkinter import Tk, Listbox
# import tkinter

root = Tk()     # 创建一个窗口
list1 = ['C', 'python', 'php', 'html', 'java']
list2 = ['CSS', 'jQuery', 'Bootstrap']
# 创建两个列表组件
com_a = Listbox(root)
com_b = Listbox(root)

# 往列表组件里写数据
for i in list1:
    com_a.insert(0, i)
for i in list2:
    com_b.insert(1, i)

# 将com_a部件放置到主窗口中
com_a.pack()
com_b.pack()
# 消息循环、事件监听
root.mainloop()



