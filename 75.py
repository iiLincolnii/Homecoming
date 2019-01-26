def find_str(arr):
    dic={}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]]+=1
        else:
            dic[arr[i]]=1
    for i in range(len(arr)):
        if dic[arr[i]]==1:
            return arr[i]
if __name__ == '__main__':
    arr=input("请输入一个字符串:")
    print(find_str(arr))
else:
    print(-1)
