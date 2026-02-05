n=int(input())
a=[]

for i in range(n):
  a.append(input().split())

a.sort(key=lambda x: int(x[0])) 

for nn in a:
  print(nn[0], nn[1])