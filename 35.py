x=int(input("请输入一个五位数:"))
if x//10000==x%10:
    if x%10000//1000==x//10%10:
        print("是")
else:
    print("不是")
