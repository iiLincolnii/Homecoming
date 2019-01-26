with open('d:/a.txt','r+') as f:a=f.read()
with open('d:/b.txt','r+') as f:b=f.read()
with open('d:/c.txt','w+') as f:f.write(a+b)
