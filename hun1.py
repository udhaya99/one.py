p=int(input())
q=list(map(int,input().split()))
so=0
but=[]
for i in range(0,p+1):
    if(q.count(i)>1):
      but.append(i)
if(len(but)==0):
    print("unique")
e=sorted(but)
print(' '.join(map(str,e)))
