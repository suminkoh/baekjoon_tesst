import sys
input = sys.stdin.readline
n=int(input())
a=[]

for i in range(n):
  a.append(int(input()))

a.sort()

print('\n'.join(map(str,a)))