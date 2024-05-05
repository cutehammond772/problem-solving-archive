import sys

sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def solve(P, A, B, G):
  # 현재 노드에서 흙의 양이 (-)이면 돈이 필요하고, (+)이면 흙이 남는다는 의미다.
  # 자식 노드에서 흙이 (-)일 경우 남는 흙이 있으면 보충하고, 아니면 합산한다.
  def work(prev, node):
    dirt = A[node] - B[node]
    
    for next in G[node]:
      if prev == next:
        continue
      
      dirt += min(0, work(node, next))
    
    return dirt
  
  return max(0, -work(0, P))

if __name__ == "__main__":
  N, P = map(int, input().split())
  A = [0, *map(int, input().split())]
  B = [0, *map(int, input().split())]
  
  G = [[] for _ in range(N + 1)]
  
  for _ in range(N - 1):
    u, v = map(int, input().split())
    
    G[u].append(v)
    G[v].append(u)
  
  print(solve(P, A, B, G))
  