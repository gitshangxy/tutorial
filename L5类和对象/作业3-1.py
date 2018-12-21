class Robot():
    Population = 0

    def __init__(self, name):
        self.name = name
        Robot.Population += 1

    def say_hi(self):
        print('大家好，我是{}'.format(self.name))

    # 1 类方法装饰器
    @classmethod
    def how_many(cls):
        print('目前总人口', cls.Population)

    # 2 静态方法装饰器
    # @staticmethod
    # def how_many():
    #     print('目前总人口',Robot.Population)

    # 3 对象方法。 不推荐这种写法
    # def how_many():           # 不推荐这种写法
    #     print('目前总人口',Robot.Population)

    def die(self):
        Robot.Population -= 1


rob1 = Robot('XR-01')
rob1.say_hi()
# Robot .how_many()
rob2 = Robot('XR-02')
Robot.how_many()
rob2.die()
Robot.how_many()