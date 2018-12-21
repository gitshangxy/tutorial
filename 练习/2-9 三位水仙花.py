# 方法一
shui=[]
for i in range(1,10):
  for j in range(10):
    for k in range(10):
      if i*i*i + j*j*j + k*k*k == 100*i + 10*j + k:
        shui.append(100*i + 10*j + k)
for i in shui:
  if i == shui[-1]:
    print(i)
  else:
    print(i, end = ',')

# 方法二
for i in range(1,10):
  for j in range(0,10):
    for k in range(0,10):
      num =  (100 * i + 10 * j + k)
      if i**3 + j**3 + k**3 == num:
        print(num)

# 方法三


