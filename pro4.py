np,mp=map(str,input().split())
t=0
if len(np)>len(mp):
	np,mp=mp,np
v=0
while v<len(np):
	  t+=(ord(mp[v])-ord(np[v]))
	  v+=1
for v in range(v,len(mp)):
	  t+=ord(mp[v])-ord('a')+1
print(t)
