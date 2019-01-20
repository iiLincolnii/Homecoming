def getcount(x):
    str=bin(x)
    count=str.count('1')
    return count
x=eval(input('请输入一个整数:'))
count=getcount(x)
print(count)
