def f(x):
    if x==1:
        return 1
    y=x*f(x-1)
    return y
print(f(5))
