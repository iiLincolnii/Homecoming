#输入猴子数量
monkey = int(input("请输入猴子数量:"))
#定义桃子总数函数
def show(n):
    #循环次数
    for i in range(1, monkey+1):
        #下一只猴子应该带走的桃子数
        t = (n - 1) / monkey
        #格式化输出
        print (u'%d. 桃子有%d个, 第%i只猴吃1个, 拿走%s个' % (i, n, i, t))
        #前一只猴子带走一份桃子后剩余的桃子总数
        n = (monkey-1) * t
#定义功能函数
def fun():
    #从1开始
    k = 1
    while True:
        t = k
        #循环次数
        for i in range(monkey-1):
            #当前猴子应拿走桃子数为tc，吃拿之前总量应为 monkey * tc + 1,前一个猴子拿走桃子数为tp，则有 (monkey-1) * tp = monkey * tc + 1
            t = monkey * t + 1
            #在for循环中含有break时则直接终止循环，不执行else
            if t % (monkey-1): break
            t /= (monkey-1)
        #当迭代的对象迭代完并为空时，位于else的子句将执行,即找到符合条件最小整数
        else:
             print (u'如果猴子%d只:'% monkey)
             print (u'桃子总数要%d个:'% (monkey * t + 1))
             show(monkey * t + 1)
             break
        k += 1
fun()
