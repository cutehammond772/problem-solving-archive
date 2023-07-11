import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

def solve(N, adj):
  result = 0
  
  queue = []
  vertices = set()

  # 초기 정점으로 1을 선택한다.
  queue.extend(adj[1])
  heapify(queue)
  
  vertices.add(1)

  # MST가 만들어질 때까지 순회를 진행한다.
  while len(vertices) < N:
    cost, node = heappop(queue)
    
    if node in vertices:
      continue

    result += cost
    vertices.add(node)
    
    for next_cost, next_node in adj[node]:
      if next_node in vertices:
        continue

      heappush(queue, (next_cost, next_node))
      
  return result

if __name__ == '__main__':
  N, M = map(int, [input(), input()])
  adj = [[] for _ in range(N + 1)]
  
  for _ in range(M):
    P, Q, R = map(int, input().split())
    
    if P == Q:
      continue
      
    adj[P].append((R, Q))
    adj[Q].append((R, P))

  print(solve(N, adj))