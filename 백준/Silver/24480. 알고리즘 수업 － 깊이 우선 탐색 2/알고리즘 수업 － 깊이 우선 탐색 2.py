import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def solve(N, R, G):
  orders = [0] * (N + 1)
  order = 1

  def traverse(node):
    nonlocal order

    orders[node] = order
    order += 1

    for next in G[node]:
      if orders[next]:
        continue

      traverse(next)

  traverse(R)
  return orders[1:]

if __name__ == "__main__":
  N, M, R = map(int, input().split())
  G = [[] for _ in range(N + 1)]

  # 1. 그래프 구성
  for _ in range(M):
    u, v = map(int, input().split())

    G[u].append(v)
    G[v].append(u)

  # 2. 인접 정점의 집합을 내림차순으로 정렬
  for node in range(1, N + 1):
    G[node].sort(reverse=True)

  result = solve(N, R, G)
  print(*result, sep='\n')
