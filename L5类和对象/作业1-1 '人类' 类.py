class People():
    def __init__(self,name,race,origin,height,weight):
        self.name = name
        self.race = race
        self.origin = origin
        self.height = height
        self.weight = weight

    def print_info(self):
        print('我叫{},我是{} 我来自{}, 身高{}, 体重{}'.format(self.name,self.race,self.origin,self.height,self.weight))

num1 = People('小明', '黄种人', '中国', 170, 70)
num2 = People('小红', '白种人', '美国', 160, 70)

num1.print_info()
num2.print_info()