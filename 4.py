year=int(input("请输入年分："))
month=int(input("请输入月份："))
day=int(input("请输入日："))
num=0
if month==1:
    num=day
elif month==2:
    num=31+day
elif month==3 and ((year%4==0 and year%100!=0) or (year%400==0)):
    if month==3:
        num=31+29+day
    if month==4:
        num=31+29+31+day
    if month==5:
        num=31+29+31+30+day
    if month==6:
        num=31+29+31+30+31+day
    if month==7:
        num=31+29+31+30+31+30+day
    if month==8:
        num=31+29+31+30+31+30+31+day
    if month==9:
        num=31+29+31+30+31+30+31+31+day
    if month==10:
        num=31+29+31+30+31+30+31+31+30+day
    if month==11:
        num=31+29+31+30+31+30+31+31+30+31+day
    if month==12:
        num=31+29+31+30+31+30+31+31+30+31+30+day
else:
    if month==3:
        num=31+28+day
    if month==4:
        num=31+28+31+day
    if month==5:
        num=31+28+31+30+day
    if month==6:
        num=31+28+31+30+31+day
    if month==7:
        num=31+28+31+30+31+30+day
    if month==8:
        num=31+28+31+30+31+30+31+day
    if month==9:
        num=31+28+31+30+31+30+31+31+day
    if month==10:
        num=31+28+31+30+31+30+31+31+30+day
    if month==11:
        num=31+28+31+30+31+30+31+31+30+31+day
    if month==12:
        num=31+28+31+30+31+30+31+31+30+31+30+day
print('第%d天'% num)
