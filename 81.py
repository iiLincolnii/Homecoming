def func():
    n = str(input("请输入四位整数:"))
    a = str((int(n[:1])+5)%10)
    b = str((int(n[1:2])+5)%10)
    c = str((int(n[2:3])+5)%10)
    d = str((int(n[3:4])+5)%10)
    number = d+c+b+a
    print(number)
func()
