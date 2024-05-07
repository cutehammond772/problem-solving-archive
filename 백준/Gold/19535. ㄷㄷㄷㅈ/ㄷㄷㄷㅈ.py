import sys, math
input = lambda: sys.stdin.readline().rstrip()

def solve(N, G, E):
  A, B = 0, 0
  
  # 'ㄷ'의 개수: 모든 간선에 대해 양끝 정점의 인접한 간선을 하나씩 뽑는 경우의 수와 같다.
  for u, v in E:
    A += (len(G[u]) - 1) * (len(G[v]) - 1)
  
  # 'ㅈ'의 개수: 모든 정점에 대해 한 정점을 기준으로 인접한 세 간선을 뽑는 경우의 수와 같다.
  for v in range(1, N + 1):
    B += math.comb(len(G[v]), 3)
  
  if A > B * 3:
    return "D"
  
  if A < B * 3:
    return "G"
  
  return "DUDUDUNGA"

if __name__ == "__main__":
  N = int(input())
  G = [[] for _ in range(N + 1)]
  E = []
  
  for _ in range(N - 1):
    u, v = map(int, input().split())
    
    G[u].append(v)
    G[v].append(u)
    
    E.append((u, v))
  
  print(solve(N, G, E))
  