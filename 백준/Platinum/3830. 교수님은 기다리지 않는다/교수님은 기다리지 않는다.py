import sys
input = lambda: sys.stdin.readline().rstrip()

def init(N):
  unions = [*range(N + 1)]
  diffs = [0] * (N + 1)

  def find(a):
    if a == unions[a]:
      return a

    route, diff = [a], [0]
    while unions[route[-1]] != route[-1]:
      route.append(unions[route[-1]])
      diff.append(diffs[route[-1]])

    total = sum(diff)
    for x in range(len(route) - 1):
      unions[route[x]] = route[-1]
      diffs[route[x]] += total
      total -= diff[x + 1]

    return unions[a]

  def union(a, b, w):
    ra, rb = find(a), find(b)

    if ra == rb:
      return

    if ra < rb:
      unions[rb] = unions[ra]
      diffs[rb] = diffs[a] + (w - diffs[b])

    elif ra > rb:
      unions[ra] = unions[rb]
      diffs[ra] = diffs[b] + (-w - diffs[a])

  def diff(a, b):
    if find(a) != find(b):
      return "UNKNOWN"

    return diffs[b] - diffs[a]

  return union, diff

if __name__ == '__main__':
  while True:
    N, M = map(int, input().split())

    if N == M == 0:
      break

    union, diff = init(N)

    for _ in range(M):
      C, *A = input().split()

      if C == '!':
        union(*map(int, A))

      elif C == '?':
        print(diff(*map(int, A)))
