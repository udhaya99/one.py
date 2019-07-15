def longe(str1,str2):
    if str1 in str2:
        return str1
    else:
        return longe(str1[0:len(str)-1],str2)
n=int(input())
list=[]
for _ in range(0,n):
    list.append(input())
list.sort()
print(longe(list[0],list[n-1]))
