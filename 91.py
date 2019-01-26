d={'a':1,'b':4,'c':2,'f':12}
a=sorted(d.items(),key=lambda x: x[1])
a1=sorted(d.items(),key=lambda x:x[1],reverse=True)
print(a1)
