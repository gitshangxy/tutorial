# 题一
# 1

f = [1,2,3,4,5]
# f = "wer"

if isinstance(f, list):
    if len(f) >= 5:
        print(f[:2])
    elif len(f) < 5:
        print('None')
else:
    print('输入错误')
    # for i in range(0,len(f)):
    #     print(f[i])

# 2
def fun(f):
    if isinstance(f,list):
        if len(f) >= 5:
            print(f[:2])
        elif len(f) < 5:
            print('None')
    else:
        print('输入错误')

f = [1,2,3,4,5]
# f1 = "qwerty"
fun(f)

# 题二

f = ['1', '2', '3', '4', '5', '6']
s = []
for i in range(0, len(f)):
    if i % 2 == 1:
        print(f[i], end='')
    s.append(f[i])
print(s)

# 题一
# 3
# f = [1,2,3,4,5]
# def i(s):
#     if len(s) < 5:
#         return None
#     elif len(s) >= 5:
#         return f[:2]
# print(i(s=f))
