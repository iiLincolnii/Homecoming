path = 'd:/test.txt'
with open(path,'w+') as f:f.write('')
while 1:
        c = input()
        if c=='#':
            break
        else:
            with open(path,'a+') as f:f.write(c)
