import time

def foo1():
    print('hello')
    print('hello', end='\n')
    print('hello')

def foo2():
    print('hello', end='')
    print('hello', end='')
    print('hello', end='')


def foo3():
    # \n 光标先回到行首，再往下一行。
    for i in range(101):
        time.sleep(0.5)
        print("Loading...{}%".format(i), end="\n")


def foo4():
    # \r 表示光标回到行首  # \n 光标先回到行首，再往下一行。
    for i in range(101):
        time.sleep(0.5)
        print("\r Loading...{}%".format(i), end="")

foo1()
foo2()
foo3()
foo4()