a,b=map(str,input().split())
if(len(a)!=len(b)):
  print("no")
else:
  v1=[a.count(j) for j in a]
  v2=[b.count(j) for j in b]
if(v1==v2):
  print("yes")
else:
  print("no")
