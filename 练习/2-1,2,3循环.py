# 1 方法一
# for n in [1, 2, 3, 4]:
#     print('****')

#方法二
# for j in range(0,4):
#     for i in range(0,4):
#         print('*', end = '')
#     print()

# 2 方法一

# for x in range(1,11):
#     for y in range(1,x + 1):
#         print('*', end = '')
#     print()



# 3 方法一
# for x in range(1,6):
#     for y in range(1,x + 1):
#         print(y, end = '')
#     print()




# 自写

def sum(r, s):
    for r in range(1, 6):
        for s in range(1, r + 1):
            print(s, end = '')
        print()
sum(1,6)




