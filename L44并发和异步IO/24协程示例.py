# 协程示例

n = 0

def consumer():
    """ 消费者 """
    r = ''
    while True:
        global n
        n = yield r
        if not n:
            return
        print('消费者 {}'.format(n))
        r = '200 OK'

def produce(c):
    # 生产者
    c.send(None)    # 相当于 next(generator)
    global n
    while n < 5:
        n = n + 1
        print('生产者 {}'.format(n))
        r = c.send(n)    # 上一次yield生产的返回值。好像书签
        print('消费者返回 {}'.format(r))
    c.close()

c = consumer()
produce(c)

"""
在produce()函数执行过程中，代码数次跳转到consu
mer(),生产返回的值又回到produce值执行。
有一点像主线程和子线程。有些像cpu运行原理。执行、挂起、回过头在执行。
"""
