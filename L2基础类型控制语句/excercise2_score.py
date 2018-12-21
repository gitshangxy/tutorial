# 接收用户输入的学生成绩，判断成绩

passed = ''
rank = ''
score = input('输入成绩:')
score = int(score)

if score < 60:
    passed = '不及格'
else:
    passed = '及格'
    if 60 <= score < 70:
         print("等级为D")
    elif 70 <= score < 80:
        print("等级为C")
    elif 80 <= score < 90:
        print("等级为B")
    elif 90 <= score <=100:
         print("等级为A")

print(passed)
print(rank)




