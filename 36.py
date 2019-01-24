letter=['M','W','F','T','S']
x=input("请输入M,W,F,T,S中的字母:")
if x==letter(0):
            print("星期一")
elif x==letter(1):
            print("星期三")
elif x==letter(2):
            print("星期五")
elif x==letter(3):
                print("请输入u或h其中一个字母:")
                if x=="u":
                    print("星期二")
                    if x=="h":
                     print("星期四")
elif x==letter(4):
                print("请输入u或a其中一个字母:")
                if x=="u":
                    print("星期天")
                    if x=="a":
                     print("星期六")
