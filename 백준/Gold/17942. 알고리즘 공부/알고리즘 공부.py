import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

# 모든 알고리즘을 배운다고 가정한 뒤, 하나씩 제외한다.
def solve(N, M, K, G):
  result = max(K)
  check = [False] * (N + 1)
  
  # 최소 M개를 유지하기 위해서는 최대 N - M개까지만 제외할 수 있다.
  count = N - M
  
  heap = [(-K[i], i) for i in range(1, N + 1)]
  heapify(heap)
  
  # 가장 많은 공부량을 가진 알고리즘부터 제거
  while count:
    amount, node = heappop(heap)
    
    if K[node] != -amount or check[node]:
      continue
    
    result = min(result, -amount)
    
    check[node] = True
    count -= 1
    
    for next, benefit in G[node]:
      if check[next]:
        continue
      
      K[next] += benefit
      heappush(heap, (-K[next], next))
  
  # 마지막에 갱신된 정보를 한 번 더 체크해야 한다.
  while -K[heap[0][1]] != heap[0][0] or check[heap[0][1]]:
    heappop(heap)
  
  return min(result, -heap[0][0])

if __name__ == "__main__":
  N, M = map(int, input().split())
  K = [0, *map(int, input().split())]
  
  R = int(input())
  G = [[] for _ in range(N + 1)]
  
  for _ in range(R):
    A, B, D = map(int, input().split())
    
    G[A].append((B, D))
    K[B] -= D
  
  print(solve(N, M, K, G))
  