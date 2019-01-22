# 生成器
"""
实际上平时一直在使用生成器
例如 range()    jieba.cut()

语法特点：yield生成项： next(生成器对象)  得到一次返回值，每次生成的值会保存到生成器对象中，下一次调用next时会从上一次的值之后往后算。好像看书一次没看完塞个书签，下一次接着书签往后看：当不断调用next知道没有值生成时会抛出异常。

优点：节省内存，生成无限大的可迭代序列。

可迭代对象：可以被for循环的
"""

def create_counter(n):
    """ 生成一条序列 """
    print('create_counter..')
    while n < 4:
        yield n    # yield 往往在循环当中
        print('increment', n)
        n += 1

cnt = create_counter(2)
print(cnt, type(cnt))   # <class 'generator'> generator 生成器对象
print(next(cnt))    # next本质调用 cnt.send(None)  cnt.send(2) 参数是上一次yield生成的值，有点像递归。send好像看书例子中看书动作，参数好像书签。
print('===')
print(next(cnt))
print(next(cnt))
print(next(cnt))  # 无法生成新项时 生成器对象StopIteration异常
print(next(cnt))


