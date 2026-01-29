n,m,v = map(int, input().split())
graph=[[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a) 


for i in range(1, n+1):
  graph[i].sort()

visited_dfs = [False]* (n+1)

def dfs(graph, v, visited):
  visited[v]=True
  print(v, end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  while queue:
    v=queue.popleft()
    print(v, end=' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i]=True

dfs(graph, v, visited_dfs)
print()
visited_bfs = [False]* (n+1)
bfs(graph, v, visited_bfs)
