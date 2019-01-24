List1=[1,2,3,4,5,6,7,8,9]
List2=[]
k=eval(input("输入非负整数k:"))
n=len(List1)
for i in range(-k,n-k):
    List2.append(List1[i])
print(List2)
