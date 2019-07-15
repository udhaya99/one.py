def longe(st1,st2):
    if st1 in st2:
        return st1
    else:
        return longe(st1[0:len(st)-1],st2)
n=int(input())
list=[]
for _ in range(0,n):
    list.append(input())
list.sort()
print(longe(list[0],list[n-1]))
