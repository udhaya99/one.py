x,n=map(int,input().split())
for i in range(x,n):
  sum=0
  temp=i
  while(temp>0):
    c=temp%10
    sum=sum+c**3
    temp=temp//10
  if(i==sum):
    print(sum,end=" ")
     
