x= int(input())
y = list(map(int,input().split()))
c = 0
for i in range(x):
    for j in range(i,x):  
        for k in range(j,x):
            if y[i]<y[j]<y[k]:
                c+=1
print(c)
