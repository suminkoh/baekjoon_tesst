n = int(input())

a=[]
for i in range(n):
  a.append(str(input().strip()))


def sumss(x):
  sums=0
  for char in x:
    if char.isdigit():
      sums+=int(char)
  return sums

a.sort(key=lambda x: (len(x), sumss(x), x ))

print('\n'.join(a))