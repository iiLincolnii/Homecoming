s=0
a=input('请输入字符串A:')
b=input('请输入字符串B:')
if len(a)>=len(b):
    for i in range(0,len(b)):
        if a[i]!=b[i]:
            a=a.replace(a[i],b[i])
            s+=2
    c=len(a)-len(b)
    print(s+c)
else:
    for p in range(0,len(a)):
        if a[p]!=b[p]:
            a=a.replace(a[p],b[p])
            s+=2
    c=len(b)-len(a)
    print(s+c)
