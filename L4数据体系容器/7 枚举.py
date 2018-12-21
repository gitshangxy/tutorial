# 枚举
# 枚举  enumerate  一个一个的列出来
# 场景：循环列表，既想获得索引、又想获得元素内容

# 1. 普通方法
name_list = ['小明', '小红', '小青']
for i in range(0, len(name_list)):
    print(i, name_list[i])

# 2. (常用)枚举 enumerate(可被迭代的对象)      Ctrl + F5  重复运行
for index,name in enumerate(name_list):
    print(index, name)

for index, attr in enumerate({'name':'小明', 'age':7, 'sex':'male'}):
    print(index,attr)

# index 索引


