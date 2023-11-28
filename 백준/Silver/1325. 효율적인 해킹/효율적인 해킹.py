import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, R):
  max_count = 0
  result = []

  for root in range(1, N + 1):
    count = 1
    visited = [False] * (N + 1)
    queue = deque([root])

    visited[root] = True

    while queue:
      node = queue.popleft()

      for next in R[node]:
        if visited[next]:
          continue

        count += 1
        visited[next] = True

        queue.append(next)

    if count > max_count:
      max_count = count
      result = [root]

    elif count == max_count:
      result.append(root)

  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  R = [[] for _ in range(N + 1)]

  for _ in range(M):
    A, B = map(int, input().split())
    R[B].append(A)

  print(*solve(N, R))
