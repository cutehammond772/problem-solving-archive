import sys, math
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def preprocess(N, adj):
  MAX = math.floor(math.log2(N)) + 1
  depths = [0] * (N + 1)
  ancestors = [[0] * MAX for _ in range(N + 1)]
  
  # 희소 배열 활용: [min, max]
  accu = [[[1000001, -1] for _ in range(MAX)] for _ in range(N + 1)]
  
  # 1번 노드의 초기 설정
  queue = deque([(1, 1)])
  
  depths[1] = 1
  ancestors[1][0] = 0
  
  while queue:
    prev, node = queue.popleft()
    depth = depths[node]
    
    for next, cost in adj[node]:
      if prev == next:
        continue
      
      depths[next] = depth + 1
      ancestors[next][0] = node
      accu[next][0] = [cost, cost]
      
      # ancestor, accumulation 설정
      for k in range(1, MAX):
        if ancestors[next][k - 1] == 0:
          break
          
        ancestors[next][k] = ancestors[ancestors[next][k - 1]][k - 1]
        
        P1 = accu[next][k - 1]
        P2 = accu[ancestors[next][k - 1]][k - 1]
        
        accu[next][k] = [min(P1[0], P2[0]), max(P1[1], P2[1])]
      
      queue.append((node, next))
  
  def solve(D, E):
    if depths[D] < depths[E]:
      D, E = E, D
    
    result = [1000001, -1]
    
    # D와 E의 depth를 맞추기
    for idx in range(MAX - 1, -1, -1):
      if depths[ancestors[D][idx]] < depths[E]:
        continue
        
      result[0] = min(result[0], accu[D][idx][0])
      result[1] = max(result[1], accu[D][idx][1])
      
      D = ancestors[D][idx]
    
    if D == E:
      return result
    
    # D와 E의 공통 조상 찾기
    for idx in range(MAX - 1, -1, -1):
      if ancestors[D][idx] == ancestors[E][idx]:
        continue

      result[0] = min(result[0], accu[D][idx][0], accu[E][idx][0])
      result[1] = max(result[1], accu[D][idx][1], accu[E][idx][1])
      
      D, E = ancestors[D][idx], ancestors[E][idx]
      
    result[0] = min(result[0], accu[D][0][0], accu[E][0][0])
    result[1] = max(result[1], accu[D][0][1], accu[E][0][1])

    return result
  
  return solve

if __name__ == '__main__':
  N = int(input())
  adj = [set() for _ in range(N + 1)]
  
  for _ in range(N - 1):
    P, Q, C = map(int, input().split())
    
    adj[P].add((Q, C))
    adj[Q].add((P, C))
  
  solve = preprocess(N, adj)
  K = int(input())
  
  for _ in range(K):
    D, E = map(int, input().split())
    print(*solve(D, E))
  