# csv
# csv 一种逗号分隔的简单语法的一种类似表格的文件存储结构，存储纯文本信息。远比数据库简单，比excel也简单。
# 场景：备份数据，适合非电脑专业人士观看。
# 准备: 新建textexcel.xlsx excel文档，编辑几行学生信息，另存csv格式。用sublime打开excel文件发现是字节信息，打开csv文件是文本信息。

import csv

# 读取数据
file_path = 'D:\\textcsv.csv'
with open(file_path) as f:
    reader = csv.reader(f)
    result = list(reader)
    # reader()方法返回对象，需要先转型成list才能看到数据 (['1', '小明'], ['2', '小红'], ['3', '小李'])
    print(result[0][1])

# 写数据
datas = [
    ['编号' '姓名', '年龄'],
    ['1', '小明', '13'],
    ['2', '小红', '11'],
    ['3', '小李', '21'],
]
with open('1testwrite.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)

    # newline='' 不写的话每写一行空一行
    # 一次写入多行
    # writer.writerows(datas)

# 以前版本
# with open('D:\\textcsv.csv') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.split(','))

"""
作业
1. 
"""