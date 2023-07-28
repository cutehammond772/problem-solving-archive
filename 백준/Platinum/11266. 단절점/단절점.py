import sys
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()

def solve(V, adj):
  discover = [0] * (V + 1)
  result = [False] * (V + 1)
  order = 0

  def traverse(node, root=False):
    nonlocal order

    discover[node] = (order := order + 1)
    child, min_node = 0, discover[node]

    for next in adj[node]:
      if discover[next]:
        min_node = min(min_node, discover[next])
        continue

      child += 1
      prev = traverse(next)

      if not root and prev >= discover[node]:
        result[node] = True

      min_node = min(min_node, prev)

    if root and child >= 2:
      result[node] = True

    return min_node

  for node in range(1, V + 1):
    if not discover[node]:
      traverse(node, True)

  return [x for x in range(V + 1) if result[x]]

if __name__ == '__main__':
  V, E = map(int, input().split())
  adj = [set() for _ in range(V + 1)]

  for _ in range(E):
    P, Q = map(int, input().split())
    adj[P].add(Q)
    adj[Q].add(P)

  points = solve(V, adj)
  print(len(points))
  print(*points)
