import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# print(json.dumps(s))
# 转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

print(json.dumps(s, default=student2dict))
# 可选参数default把任意一个对象变成一个可序列为JSON的对象
# 需要为Student专门写一个转换函数，再把函数传进去即可：
# 使用__dict__代替person2dict函数，再使用lambda函数简化。
# print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))


"""
对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数
"""