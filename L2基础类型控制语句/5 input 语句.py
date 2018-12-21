#input语句
number = 20

user_number = input('请输入一个数字：')
user_number = int(user_number)

if user_number > number:
    print('猜大了')
elif user_number < number:
    print('猜小了')
else:
    print('猜对了')


"""
input(): 接收用户输入，返回字符串。
"""