a,b=input().split()
l=len(a) if len(a)<len(b) else len(b)
d=abs(len(a)-len(b))
count=d
for i in range(l):
  if(len(b)==1 and b[i] in a):
    break
  if(a[i]!=b[i]):
    count+=1
print(count)
