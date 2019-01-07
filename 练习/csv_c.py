import csv

# csv读文件与写文件 表格式。

# 从csv文件中读取数据
# filename = 'D:/pycharm尚小雨/tutorial/练习/csv_cd.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     # data不能直接打印，list(data)最外层是list，里层的每一行数据都在一个list中   [['name', 'age'], ['Bob', '11'], ['Tom', '21'], ...]
#     # print(list(reader))
#     # 读取一行，下面的reader中已经没有该行了。行号从2开始
#     hesd_row = next(reader)
#     for row in reader:
#         # 行号从1开始， 可以用reader.line_num获取
#         print(reader.line_num, row)
#         # reader只能被遍历一次。由于reader是可迭代对象，可以使用next方法一次获取一行。


# 写数据到csv文件中
# reader读取，writer写入。一次写入一行，一次写入多行都可
# 使用数字或字符串的数字都可以
datas = [['name', 'age'],
         ['Bob', 11],
         ['Tom', '23'],
         ['Jerry', '18']]
with open('csv_cw.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)
        # 写入多行。 不指定newline='',则每写入一行将有一空行被写入
        writer.writerows(datas)


"""
CSV(Comma-Separated Values)即逗号分隔值，可以用Excel打开查看。
由于是纯文本，任何编辑器也都可打开。
与Excel文件不同，CSV文件中：
- 值没有类型，所有值都是字符串
- 不能指定字体颜色等样式
- 不能指定单元格的宽高，不能合并单元格
- 没有多个工作表
- 不能嵌入图像图表

在CSV文件中，以,作为分隔符，分隔两个单元格。
像这样a,,c表示单元格a和单元格c之间有个空白的单元格。依此类推。

"""