a=[1,3,5,7,9,11,13,15,17,19,0]         
number=int(input("请输入要插入的数字:"))
if number>a[9]:
    a[10]=number
else:
    for i in range(10):
        if(number<a[i]):                            
            temp1=a[i]
            a[i]=number
            for j in range(i+1,11):
                temp2=a[j]
                a[j]=temp1
                temp1=temp2
            break
print(a) 
