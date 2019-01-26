import random
num=[]
s=['*']
for i in range(0,3):
    num.append(random.randint(1,10)) 
    print(" *个数为:",num[i])
    print('*'*num[i])
