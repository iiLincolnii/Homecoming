a=[6,3,10,2,5,1,4,7,9,8]
i=a.index(max(a))
a[0],a[i]=a[i],a[0]
i=a.index(min(a))
a[-1],a[i]=a[i],a[-1]
print(a)
