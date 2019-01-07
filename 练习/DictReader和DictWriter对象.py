import csv

# 读取文件 DictReader
# filename = 'D:/pycharm尚小雨/tutorial/练习/csv_cd.csv'
# with open(filename) as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         # name是表第一行的某个数据，作为key
#         max_temp = row['name']
#         print(max_temp)


# 读文件 DictWriter类
headers = ['name', 'age']

datas = [{'name': 'Bob', 'age': 23},
        {'name': 'Jerry', 'age': 44},
        {'name': 'Tom', 'age': 15}
        ]
with open('csv_cw.csv', 'w', newline='') as f:
    # 标头在这里传入，作为第一行数据
    writer = csv.DictWriter(f, headers)
    writer.writeheader()
    for row in datas:
        writer.writerow(row)
        # 还可以写入多行
        writer.writerows(datas)


"""
使用DictReader可以像操作字典那样获取数据，把表的第一行（一般是标头）作为key。
可访问每一行中那个某个key对应的数据。
使用DictWriter类，可以写入字典形式的数据，同样键也是标头（表格第一行）

"""