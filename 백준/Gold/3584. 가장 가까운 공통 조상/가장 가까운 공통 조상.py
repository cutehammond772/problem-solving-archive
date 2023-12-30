import sys
sys.setrecursionlimit(11111)
input = lambda: sys.stdin.readline().rstrip()

def find(G, X, R):
  # 최종 결과
  result = []

  # DFS
  route = [R]

  def traverse():
    nonlocal result
    node = route[-1]

    if result:
      return

    if node == X:
      result = route[:]
      return

    for node in G[route[-1]]:
      route.append(node)
      traverse()
      route.pop()

  traverse()
  return result

def solve(G, P, Q, R):
  p_route = find(G, P, R)
  q_route = find(G, Q, R)

  offset = 0
  result = -1

  while offset < len(p_route) and offset < len(q_route) and p_route[offset] == q_route[offset]:
    result = p_route[offset]
    offset += 1

  return result

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    N = int(input())
    G = [[] for _ in range(N + 1)]

    # 루트 판별을 위한 진입 차수 계산
    degree = [0] * (N + 1)

    for _ in range(N - 1):
      A, B = map(int, input().split())

      degree[B] += 1
      G[A].append(B)

    P, Q = map(int, input().split())
    R = max([node for node in range(1, N + 1) if degree[node] == 0])

    print(solve(G, P, Q, R))
