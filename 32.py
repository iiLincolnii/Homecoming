str=input('请输入五位字符:')
for i in range(0, len(str)):
 print(str[len(str)-i-1],end='')
