# python字典和互通结构json 互相转化

import json

student_list = [
    {'no': 1, 'name': '小明', 'age': 13},
    {'no': 2, 'name': '小红', 'age': 10},
    {'no': 3, 'name': '小李', 'age': 9}
]

student_json = """
{
    "student_list" : [
        {"no": 1, "name": "小明", "age": 13},
        {"no": 2, "name": "小红", "age": 10},
        {"no": 3, "name": "小李", "age": 9}
    ],
    "school_name": "智游",
    "address": "财富天街"
}
"""

# 对象转json  （序列化）
stu_json = json.dumps(student_list, indent=4)
print(type(stu_json), stu_json)
"""
json.dumps(数据对象) 返回json格式字符串。
形如\u5c0f是中文的unicode编码。计算机传输的本质是二进制信息。
"""
# json转对象
stu_obj = json.loads(student_json)
print(stu_obj)
for stu in stu_obj['student_list']:
    print(f'学生姓名{stu["name"]}')

# json.dump()  json.load()  这两个方法的参数是文件
# dumps()  load() 参数是变量

with open('7天气接口返回数量.json', encoding='utf-8') as file:
    weather_obj = json.load(file)
    print(weather_obj)

# 可能出现的错误：
# json解析错误。检查json双引号，逗号，缩进是否正确。
# 面试题：
# json.dump()和dumps()区别