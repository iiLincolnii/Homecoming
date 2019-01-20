n=int(input("请输入一个数:"))
if n%2==0:
    way=(n/2)+1
else:
    way=(n+1)/2
print("%d 种方法可以爬上楼."%way)
