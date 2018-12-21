count=0
for i in range(10000,100000):
    a=str(i)
    if a[0]==a[4] and a[1]==a[3]:
        print(a)
        count+=1
print("共有五位回文数:%d"%count)