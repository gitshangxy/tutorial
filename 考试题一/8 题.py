# 已知列表，求最大值


list1 = [2, -1, 5, 0, 99, -1]

def get_max3(list1):
    nummax = list1[0]
    for i in list1:
        if i > nummax:
            nummax = i
    return nummax

print(get_max3(list1))
