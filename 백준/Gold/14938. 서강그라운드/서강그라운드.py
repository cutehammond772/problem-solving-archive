import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, x, items, edges):
  queue = []
  visited = [False] * N
  result = 0
  
  heappush(queue, (0, x))
  
  while len(queue) != 0:
    accu_cost, node = heappop(queue)
    if visited[node]:
      continue
    
    visited[node] = True
    result += items[node]
    
    for next, cost in edges[node]:
      if accu_cost + cost > M or visited[next]:
        continue
        
      heappush(queue, (accu_cost + cost, next))

  return result

if __name__ == '__main__':
  N, M, R = map(int, input().split())
  items = list(map(int, input().split()))
  edges = [[] for _ in range(N)]
  
  for _ in range(R):
    A, B, L = map(int, input().split())
    edges[A - 1].append((B - 1, L))
    edges[B - 1].append((A - 1, L))
    
  print(max([solve(N, M, x, items, edges) for x in range(N)]))