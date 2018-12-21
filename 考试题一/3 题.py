# 输入成绩， 判断评分

def sum1(score):
    if 90 <= score <= 100:
        print("等级为A")
    elif 80 <= score <= 89:
        print("等级为B")
    elif 70 <= score <= 79:
        print("等级为C")
    elif 60 <= score <= 69:
        print("等级为D")
    elif 0 <= score < 60:
        print("等级为F")
    else:
        print('输入不合法')


sum1(-7)

