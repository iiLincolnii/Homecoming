for i in range(1,1001):
      t=i           
      sum=0       
      x=2
      while x<i:         
          if i%x==0:
              sum+=x
              x+=1
          else:
              x+=1
          if sum+1==t:
              print(t)
