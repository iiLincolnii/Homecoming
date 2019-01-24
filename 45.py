print('第一个列表')
l1=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
   print(l1[i])
print('第二个列表')
l2=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(3):
   print(l2[i])
print('第三个列表为两个列表同位置的数相加构成')
l3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(l1)):
  for j in range(len(l1[i])):
     l3[i][j]=l1[i][j]+l2[i][j]
print('输出第三个列表为:')
for i in range(3):
   print(l3[i])
