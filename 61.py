ls=[]
for i in range(3):
    x=input("请输入数字:")
    ls.append(x)
ls.sort()
print(ls[::-1])
