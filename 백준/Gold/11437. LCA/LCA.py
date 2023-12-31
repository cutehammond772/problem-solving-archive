import sys
from collections import deque

DEPTH = 17
input = lambda: sys.stdin.readline().rstrip()

# 정점 1을 루트로 하는 트리의 ancestor sparse table을 생성한다.
def init(N, T):
  # ancestors[node][k] : node의 2^k번째 조상
  ancestors = [[0] * DEPTH for _ in range(N + 1)]
  depths = [0] * (N + 1)

  # (부모 노드, 현재 노드, 깊이)
  queue = deque([(0, 1, 1)])

  while queue:
    prev, node, depth = queue.popleft()

    # 현재 노드의 깊이
    depths[node] = depth

    # 부모 노드 = 1번째 조상
    ancestors[node][0] = prev

    for k in range(1, DEPTH):
      ancestors[node][k] = ancestors[ancestors[node][k - 1]][k - 1]

    for next in T[node]:
      if prev == next:
        continue

      queue.append((node, next, depth + 1))

  return ancestors, depths

# 두 노드의 최소 공통 조상을 구한다.
def lca(ancestors, depths, u, v):
  # 1. 두 노드의 깊이를 동일하게 맞춘다.

  if depths[u] > depths[v]:
    # v의 깊이를 낮추어 u와 맞추는 방향으로 간다.
    u, v = v, u

  for depth in range(DEPTH - 1, -1, -1):
    next_v = ancestors[v][depth]

    if depths[next_v] >= depths[u]:
      v = next_v

  # 2. 최소 공통 조상을 구한다.
  if u == v:
    return u

  for depth in range(DEPTH - 1, -1, -1):
    next_u, next_v = ancestors[u][depth], ancestors[v][depth]

    if next_u != next_v:
      u, v = next_u, next_v

  return ancestors[u][0]

def solve(N, T, Q):
  ancestors, depths = init(N, T)
  result = []

  for u, v in Q:
    result.append(lca(ancestors, depths, u, v))

  return result

if __name__ == "__main__":
  # 1. 트리 T 입력
  N = int(input())
  T = [[] for _ in range(N + 1)]

  for _ in range(N - 1):
    u, v = map(int, input().split())

    T[u].append(v)
    T[v].append(u)

  # 2. 쿼리 Q 입력
  M = int(input())
  Q = []

  for _ in range(M):
    u, v = map(int, input().split())
    Q.append((u, v))

  # 3. LCA 쿼리 처리 및 출력
  result = solve(N, T, Q)
  print(*result, sep='\n')
