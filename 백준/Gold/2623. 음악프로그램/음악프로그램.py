import sys
from queue import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, degrees, adj):
  result = []
  visited = [False] * N
  que = deque()

  for x in [x for x in range(N) if degrees[x] == 0]:
    que.append(x)
    visited[x] = True
    
  while que:
    x = que.popleft()
    result.append(x + 1)

    for t in adj[x]:
      if visited[t]:
        continue

      degrees[t] -= 1
      
      if degrees[t] == 0:
        visited[t] = True
        que.append(t)

  if len(result) < N:
    return [0]
    
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  degrees = [0] * N
  adj = [[] for _ in range(N)]
  
  for _ in range(M):
    K, *orders = map(int, input().split())
    
    for x in range(K - 1):
      curr, next = orders[x] - 1, orders[x + 1] - 1
      
      adj[curr].append(next)
      degrees[next] += 1
      
  print(*solve(N, degrees, adj), sep='\n')