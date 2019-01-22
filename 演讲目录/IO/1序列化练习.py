import pickle      # 实现序列化
d = dict(name='Bob', age=20, score=88)
L1 = pickle.dumps(d)     # 序列化为字节   或用pickle.dump()直接把对象序列化后写入一个file-like Object：
print(L1)


f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象
# pickle.load()方法从一个file-like Object中直接反序列化出对象
f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

"""
变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling
反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling(拆封)。
"""


"""
JSON表示出来就是一个字符串，可以被所有语言读取，方便地存储到磁盘或者通过网络传输。
标准格式 速度快

dumps()方法返回一个str。dump()方法可以直接把JSON写入一个file-like Object。
把json反序列化为Python对象，loads()方法把JSON的字符串反序列化，load()从file-like Object中读取字符串并反序列化：
"""
# import json
# d = dict(name='Bob', age=20, score=88)
# L2 = json.dumps(d)
# print(L2)
#
# json_str = '{"age": 20, "score": 88, "name": "Bob"}'
# js = json.loads(json_str)
# print(js)


"""
序列化：把对象转换为字节序列的过程称为对象的序列化。
反序列化：把字节序列恢复为对象的过程称为对象的反序列化。


通过将对象序列化可以将其存储在变量或者文件中，可以保存当时对象的状态，实现其生命周期的延长
"""