# 1
# s = input('随意输入字符串： ')
# a = 0
# b = 0
# c = 0
# d = 0
# for i in s:
#     print(i)
#     if i.isdigit():
#        a = a + 1
#
#     elif i.isalpha():
#         b += 1
#     elif i.isspace():
#         c += 1
#     else:
#         d += 1
#
# print('数字个数有：' + str(a) + '个')
# print('字母个数有：' + str(b) + '个')
# print('空格个数有：' + str(c) + '个')
# print('特殊字符个数有：' + str(d) + '个')
#2
alpha_num = 0
digit_num = 0
space_num = 0
other_num = 0

user_input = input('随意输入:')
for i in user_input:
    if i.isalpha():
        alpha_num += 1
    elif i.isdigit():
        digit_num += 1
    elif i.isspace():
        space_num += 1
    else:
        other_num += 1
print('字母{}，数字{}，空格{}，其它{}'.format(alpha_num, digit_num, space_num, other_num))