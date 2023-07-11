import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

def solve(N, edges, degrees):
  result = []
  visited = [False] * N
  
  # 진입 차수가 0인 노드를 출발점으로 함
  queue = [x for x in range(N) if degrees[x] == 0]

  for x in queue:
    visited[x] = True
    
  # 노드의 번호가 빠른 것이 먼저 나오도록 함
  heapify(queue)

  while queue:
    node = heappop(queue)
    result.append(node + 1)
    
    for next in edges[node]:
      if visited[next]:
        continue

      degrees[next] -= 1
      
      if degrees[next] == 0:
        heappush(queue, next)
        visited[next] = True
        
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  edges = [[] for _ in range(N)]
  degrees = [0] * N

  for _ in range(M):
    A, B = map(int, input().split())
    
    edges[A - 1].append(B - 1)
    degrees[B - 1] += 1

  print(*solve(N, edges, degrees))