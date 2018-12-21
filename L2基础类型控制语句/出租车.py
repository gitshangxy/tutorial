# 输入公里数，自动计算

kilometer = int(input("输入公里数："))

if  kilometer <= 0:
    print("输入错误")
elif  0 <= kilometer <= 2:
    price = 8
    print(price)
elif  2 < kilometer < 12:
    price = 8 + 1.2 * (kilometer - 2)
    print(price)
elif kilometer >12:
    price = 8 + 1.2 * (kilometer - 2) + 1.5 * (kilometer - 12)
    print(price)

