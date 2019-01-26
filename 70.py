def even(num):
    s = 0
    for i in range(2, num+1, 2):
        s += 1 / i
    return s

def podd(num):
    s = 0
    for i in range(1, num+1, 2):
        s += 1 / i
    return s

def dcall(fp, n):
    s = fp(n)
    return s

if __name__ == "__main__":
    num = int(input("请输入一个整数："))
    if num % 2 == 0:
        print("偶数")
        sum = dcall(even,num)
    else:
        print("奇数")
        sum = dcall(podd, num)
    print(sum)
