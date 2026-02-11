n=int(input())
n_having=list(map(int,input().split()))
m=int(input())
m_card=list(map(int, input().split()))

def check_having(array, target, start, end):
  while start <= end:
    mid=(start+end)//2
    if array[mid]==target:
      return mid
    elif array[mid] > target:
      end=mid-1
    else:
      start=mid+1
  return None

n_having.sort()


for target in m_card:
    result = check_having(n_having, target, 0, n - 1)
    if result is not None: 
        print(1, end=' ')
    else:
        print(0, end=' ')