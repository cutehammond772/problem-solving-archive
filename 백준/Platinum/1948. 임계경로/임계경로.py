import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def solve(N, start, dest, degrees, adjacents):
  memo = [[0, []] for _ in range(N + 1)]
  queue = deque([start])

  # 모두가 도착하는 시간 구하기
  while queue:
    node = queue.popleft()
    cumulation = memo[node][0]
    
    for next, cost in adjacents[node]:
      degrees[next] -= 1
      next_cumulation = memo[next][0]
      
      if next_cumulation < cumulation + cost:
        memo[next] = (cumulation + cost), [(node, next)]
      elif next_cumulation == cumulation + cost:
        memo[next][1].append((node, next))
        
      if degrees[next] == 0:
        queue.append(next)
        
  # 경로를 역추적하여 도착 시간과 동일한 경로의 수 구하기
  routes = set()
  queue.extend(memo[dest][1])

  while queue:
    prev, curr = queue.popleft()
    
    if (prev, curr) not in routes:
      routes.add((prev, curr))
      queue.extend(memo[prev][1])
  
  return memo[dest][0], len(routes)

if __name__ == '__main__':
  N, M = map(int, [input(), input()])
  adjacents = [[] for _ in range(N + 1)]
  degrees = [0] * (N + 1)
  
  for _ in range(M):
    node, next, cost = map(int, input().split())

    degrees[next] += 1
    adjacents[node].append((next, cost))

  start, dest = map(int, input().split())
  print(*solve(N, start, dest, degrees, adjacents), sep='\n')