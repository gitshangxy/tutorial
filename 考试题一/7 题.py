# 去重

list1 = [1, 2, 3, 2, 1, 4, 5]
new_list = []
for i in list1:
    if i not in new_list:
        new_list.append(i)
print(new_list)