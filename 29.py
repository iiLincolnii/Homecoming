n=int(input('请输入要计算的整数：'))
a=1
x=0
for i in range(1,n+1):
    num=i
for j in range(i-1,0,-1):
    num*=j
x+=num
print(x)
