a,b=map(int,input().split())
for i in range(a+1,b):
    if(i%2==0):
        continue
    else:
        print(i)
