# 类的继承

"""
引题：生活例子，手机类，oppo手机、华为手机看作是手机类里的对象：但oppo手机也可以称作一个类，这个类下又包含find系列、R系列，R系列类又包含某某具体型号对象。类有包含、继承的关系。
"""
# 引题2：写一个教师类：属性name age sex salary subject address phone ,方法say_hi(), go_work()。
# 再写一个学生类：属性name age sex hobby parent_info,方法say_hi(), go_class()。
# 再写一个行政人员类

class Teacher():
    def __init__(self, name, age, sex, salary, subject, address):
        self.name = name
        self.age = age
        self.sex = sex
        self.salary = salary
        self.subject = subject
        self.address = address

    def say_hi(self):
        print('hello')

    def go_work(self):
        pass

class Student():
    def __init__(self, name , age, sex, hobby, parent_info):
        self.name = name
        self.age = age
        self.sex = sex
        self.hobby = hobby
        self.parent_info = parent_info

    def say_hi(self):
        print('hello')

    def go_class(self):
        pass


# 继承：未使用继承前，代码如上，类与相似的类有重复的属性、方法，书写麻烦。
# 所以python引入了类继承机制。继承是类的三大特性之一。
class Animal(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print('动物在跑')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog1 = Dog('臭臭')
dog1.run()
cat1 = Cat('小花')
cat1.run()


"""
父类：上例中 Animal(动物)类逻辑上、范围上包含Dog、Cat类。那么我们把Animal类叫做
“父类”、“超类”、“基类”：Dog、Cat类就叫做“子类”、“衍生类”

继承：语法 类定义时，类名后面小括号里填写父类名。注意跟类实例化时、函数后面的小括号里的内容不一样。

object: python中变量、方法万物皆对象，现实生活中也是万物皆对象。为了面向对象体质完整，定义了一个默认的、抽象的顶级对象object。object是所有类的父类。每一个类都默认继承object类，具备一些关于类的基础方法如__init__  __del__。

子类继承父类所有的属性、方法:Dog类实例化用的是父类Animal类中的__init__()  rin()。例如华为手机类拥有的父类手机类打电话、发短信功能。

场景：类比较多而且相似的时候，适合抽象为父类、子类，比如游戏。过度抽象可能会使问题更加复杂，
好处：类与类关系更加清晰；代码量少；公共部分抽象出来，扩展更加方便。
"""
