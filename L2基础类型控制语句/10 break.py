# 需求： 软件需要有退出的功能。循环中达到我们想象的条件是退出。节省计算机资源。
# 循环的中断

while True:
    s = input('随便输入点什么:')

    if s == 'quit':
        break

    print('你输入的字符串长度是{}'.format(len(s)))

print('完')

# break:退出循环。跳出循环语句块。
# len(d对象)：返回对象的长度。