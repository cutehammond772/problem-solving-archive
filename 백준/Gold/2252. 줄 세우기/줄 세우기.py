import sys
from queue import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, in_degrees, adjacents):
  result = []
  
  que = deque()
  visited = [False] * N

  for x in [x for x in range(N) if in_degrees[x] == 0]:
    que.append(x)
    visited[x] = True
  
  while que:
    x = que.popleft()
    result.append(x + 1)
    
    for t in adjacents[x]:
      if visited[t]:
        continue
        
      in_degrees[t] -= 1
      
      if in_degrees[t] == 0:
        que.append(t)
        visited[t] = True
        
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  in_degrees = [0] * N
  adjacents = [[] for _ in range(N)]
  
  for _ in range(M):
    P, Q = map(int, input().split())
    adjacents[P - 1].append(Q - 1)
    in_degrees[Q - 1] += 1
    
  result = solve(N, in_degrees, adjacents)
  print(*result)