# open() 更多模式

"""
open()第二个参数mode模式：
'r', read   读取信息
'w', write   写信息
'rb', read byte  读取字节信息
'wb', write byte  写字节信息

"""
with open('8 with.txt', 'w', encoding='utf-8') as f:
    f.write('hello\n')
    f.write('小明\n')
    f.write('很高兴')
    f.write('认识你')


with open('8 with.txt', 'w', encoding='utf-8') as f:
    f.write('第二次写入信息')

"""
w 写模式，每一次打开文件写信息，会将之前的信息覆盖掉。
"""

with open('8 with.txt', 'a', encoding='utf-8') as f:
    f.write('\na模式会追加信息到文件末尾')

"""
a模式append，打开文件并追加写入信息。
r+ 打开文件用于读写。
ab 追加写二进制信息。
"""


