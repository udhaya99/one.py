m,n=input().split()
l=len(m) if len(m)<len(n) else len(n)
u=abs(len(m)-len(n))
count=u
for i in range(l):
  if(len(n)==1 and n[i] in m):
    break
  if(m[i]!=n[i]):
    count+=1
print(count)
