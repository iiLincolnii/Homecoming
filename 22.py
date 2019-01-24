def main():
    basis=int(input("输入一个基础数: "))
    n=int(input('输入该数长度: '))
    arr=[0]*n
    b=basis
    sum=0
    for i in range(n):
        arr[i]=basis
        sum +=basis
        basis=basis * 10 + b
    print("%d="%sum,end='')
    for i in range(n):
        print("%d"%arr[i],end='')
        if i < n-1:
            print("+",end='')
if __name__=='__main__':
    main()
