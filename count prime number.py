a1,a2=map(int,input().split())
a3=[]
for b in range (a1,a2+1):
  for c in range(2,b):
    if (b%c==0):
      break
  else:
      a3.append(b)
print(len(a3))
