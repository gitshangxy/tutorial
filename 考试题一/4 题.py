# 接收用户输入的年份，判断年份是否为闰年

def year():
    num_year = int(input('请输入一个年份：'))
    if num_year % 4 == 0 or num_year % 400 == 0:
        print("该年份为闰年")
    else:
        print('该年份为平年')
year()