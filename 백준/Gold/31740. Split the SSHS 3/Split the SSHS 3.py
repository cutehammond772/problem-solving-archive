import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()
MAX = int(1e18)

def solve(N, G, W):
  memo = [0] * (N + 1)
  result = (MAX, 0, 0)
  
  # Tree DP
  def accumulate(prev, node):
    memo[node] = W[node]
    
    for next in G[node]:
      if prev == next:
        continue
        
      accumulate(node, next)
      memo[node] += memo[next]
  
  # 최소 찾기
  def traverse(prev, node):
    nonlocal result
    
    for next in G[node]:
      if prev == next:
        continue
      
      result = min(result, (abs(memo[next] - (memo[1] - memo[next])), node, next))
      traverse(node, next)
  
  # 1을 루트로 한다.
  accumulate(0, 1)
  traverse(0, 1)
  
  return result

if __name__ == "__main__":
  N = int(input())
  G = [[] for _ in range(N + 1)]
  
  for _ in range(N - 1):
    P, Q = map(int, input().split())
    
    G[P].append(Q)
    G[Q].append(P)
  
  W = [0] * (N + 1)
  
  for i in range(1, N + 1):
    W[i] = int(input())
  
  result, n1, n2 = solve(N, G, W)
  
  print(result)
  print(n1, n2)
  