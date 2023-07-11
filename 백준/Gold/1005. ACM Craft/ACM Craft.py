import sys
from queue import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, W, costs, degrees, adjacents):
  que = deque()
  visited = [False] * N
  memo = [0] * N
  
  for x in [x for x in range(N) if degrees[x] == 0]:
    que.append(x)
    visited[x] = True
    memo[x] = costs[x]

  while que:
    x = que.popleft()
    
    if x == W:
      continue

    for t in adjacents[x]:
      if visited[t]:
        continue

      degrees[t] -= 1
      memo[t] = max(memo[t], memo[x] + costs[t])
      
      if degrees[t] == 0:
        que.append(t)
        
  return memo[W]

if __name__ == '__main__':
  T = int(input())
  
  for _ in range(T):
    N, K = map(int, input().split())
    costs = list(map(int, input().split()))
    degrees = [0] * N
    adjacents = [[] for _ in range(N)]
    
    for _ in range(K):
      P, Q = map(int, input().split())
      adjacents[P - 1].append(Q - 1)
      degrees[Q - 1] += 1

    W = int(input())
    print(solve(N, W - 1, costs, degrees, adjacents))