import sys
sys.setrecursionlimit(10 ** 6 + 1)
input = lambda: sys.stdin.readline().rstrip()

def solve(V, adj):
  result = []

  discover = [0] * (V + 1)
  order = 0

  def traverse(node, root):
    nonlocal order

    discover[node] = (order := order + 1)
    min_node = discover[node]

    for next in adj[node]:
      if next == root:
        continue

      if discover[next]:
        min_node = min(min_node, discover[next])
        continue

      prev = traverse(next, node)

      if prev > discover[node]:
        result.append((min(node, next), max(node, next)))

      min_node = min(min_node, prev)

    return min_node

  for node in range(1, V + 1):
    discover[node] or traverse(node, 0)

  return sorted(result)

if __name__ == '__main__':
  V, E = map(int, input().split())
  adj = [set() for _ in range(V + 1)]

  for _ in range(E):
    P, Q = map(int, input().split())
    adj[P].add(Q)
    adj[Q].add(P)

  lines = solve(V, adj)
  print(len(lines))

  for x, y in lines:
    print(x, y)
