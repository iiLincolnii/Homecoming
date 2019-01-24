n=int(input('请输入项数:'))
x=2
y=1
l=[]
s=0
for i in range(1,n+1):
    a=x
    b=y

    s+=(a/b)
    l.append('%s/%s'%(a,b))
    x=a+b
    y=a
print('+'.join(str(i) for i in l),end = '')
print('=%.2f'%s)
