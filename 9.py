a,b=input().split()
b=int(b)
l=list(map(int,input().split())) 
sum=0
for i in range(0,b):
  sum+=l[i]
print(sum)
