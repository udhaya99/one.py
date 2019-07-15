import math
x=int(input())
l=list(map(int,input().split()))
l.sort()
a=len(l)
b=math.ceil(a/2)
print(b)
