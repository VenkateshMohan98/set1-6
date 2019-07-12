vk=input()
vk=vk.split()
ais=vk[0]
b=vk[1]
count=0
a=0
while(a<len(ais) and count<2):
  if (ais[a]!=b[a]):
    count+=1
  a+=1
if(count==1 or count==0):
  print("yes")
else:
  print("no")
