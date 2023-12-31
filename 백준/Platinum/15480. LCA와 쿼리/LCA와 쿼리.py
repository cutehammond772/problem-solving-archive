import sys
from collections import deque

DEPTH = 18
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

  for r, u, v in Q:
    # u, v의 최소 공통 조상을 서브트리의 루트로 정의한다.
    root = lca(ancestors, depths, u, v)
    lca_ur = lca(ancestors, depths, u, r)
    lca_vr = lca(ancestors, depths, v, r)
    lca_rr = lca(ancestors, depths, root, r)

    # Case 1. u, v를 루트로 하는 서브트리가 한 쪽에 포함 관계인 경우
    if root == u or root == v:
      # Case 1-1. u, v 아래에 존재하는 경우
      if lca_ur == u and lca_vr == v:
        if depths[u] >= depths[v]:
          result.append(u)
        else:
          result.append(v)

      # Case 1-2. u, v 중간에 존재하는 경우
      elif lca_ur == u and lca_vr != v:
        result.append(lca_vr)

      elif lca_ur != u and lca_vr == v:
        result.append(lca_ur)

      # Case 1-3. u, v 위에 존재하는 경우
      else:
        result.append(root)

    # Case 2. u, v를 루트로 하는 서브트리가 서로 독립 관계인 경우
    else:
      # Case 2-1. r가 "u를 루트로 하는 서브트리" 내에 존재하면, lca는 u이다.
      if lca_ur == u:
        result.append(u)

      # Case 2-2. r가 "v를 루트로 하는 서브트리" 내에 존재하면, lca는 v이다.
      elif lca_vr == v:
        result.append(v)

      # Case 2-3. r가 Case 1.2.를 제외한 위의 서브트리 내에 존재하는 경우
      elif lca_rr == root:
        if (lca_ur == r and lca_vr == root) or (lca_ur == root and lca_vr == r):
          result.append(r)

        elif lca_ur != r and lca_vr == root:
          result.append(lca_ur)

        elif lca_ur == root and lca_vr != r:
          result.append(lca_vr)

        else:
          result.append(root)

      # Case 2-4. r가 서브트리 밖에 존재하는 경우, 그대로 서브트리의 루트가 lca가 된다.
      else:
        result.append(root)

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
    r, u, v = map(int, input().split())
    Q.append((r, u, v))

  # 3. LCA 쿼리 처리 및 출력
  result = solve(N, T, Q)

  for node in result:
    print(node)
