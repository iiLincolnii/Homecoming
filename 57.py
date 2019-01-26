l=[1]
print(l)
l.append(0)
n=10
for i in range(1,n):
    newline=[]
    for j in range(i+1):
        value=l[j]+l[-j-1]
        newline.append(value)
    print(newline)
    l=newline
    l.append(0)
