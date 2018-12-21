# 手机类

class Phone():
    def __init__(self, brand, price, stock):
        self.brand = brand
        self.price = price
        self.stock = stock

    def print_info(self):
        print('手机品牌{},价格{},库存数量{}'.format(self.brand,self. price,self.stock))

num1 = Phone('华为', 3400, 1000)
num2 = Phone('小明', 3000, 900)

num1.print_info()
num2.print_info()

