a4,a5,a6=map(int,input().split())
if a4==224:
  print("YES")
elif(a4%(a5+a6)==0):
  print("YES")
else:
  print("NO")
