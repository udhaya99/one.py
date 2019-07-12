def longest(strg1,strg2):
    if strg1 in strg2:
        return strg1
    else:
        return longest(strg1[0:len(strg)-1],strg2)
n=int(input())
list=[]
for _ in range(0,n):
    list.append(input())
list.sort()
print(longest(list[0],list[n-1]))
