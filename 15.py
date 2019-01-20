x=[]
for i in range(1,10):
  for j in range(10):
    for k in range(10):
      if i*i*i + j*j*j + k*k*k == 100*i + 10*j + k:
        x.append(100*i + 10*j + k)
for i in x:
  if i == x[-1]:
    print(i)
  else:
    print(i, end = ',')
