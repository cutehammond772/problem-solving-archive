import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
MAX = 14

def solve(N, ants, adj):
  result = []
  
  ancestors = [[0] * MAX for _ in range(N + 1)]
  depths = [0] * (N + 1)
  distances = [0] * (N + 1)
  queue = deque([(1, 1)])
  
  while queue:
    prev, node = queue.popleft()
    depth, distance = depths[node], distances[node]
    
    ancestors[node][0] = prev
    for idx in range(1, MAX):
      ancestors[node][idx] = ancestors[ancestors[node][idx - 1]][idx - 1]
    
    for next, cost in adj[node]:
      if prev == next:
        continue
        
      depths[next] = depth + 1
      distances[next] = distance + cost
      queue.append((node, next))
  
  for x in range(1, N + 1):
    cost, current = ants[x], x
    
    if distances[current] <= cost:
      result.append(1)
      continue
    
    for idx in range(MAX - 1, -1, -1):
      node = ancestors[current][idx]
      required_cost = distances[current] - distances[node]
      
      if required_cost > cost:
        continue
      
      cost -= required_cost
      current = node
    
    result.append(current)
  
  return result

if __name__ == '__main__':
  N = int(input())
  ants = [0] + [int(input()) for _ in range(N)]
  adj = [set() for _ in range(N + 1)]
  
  # 트리 생성
  for _ in range(N - 1):
    P, Q, C = map(int, input().split())
    adj[P].add((Q, C))
    adj[Q].add((P, C))
  
  result = solve(N, ants, adj)
  print(*result, sep='\n')
  