import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, tree, degrees):
  result = []

  # 필요한 총 부품의 개수
  counts = [0] * (N + 1)
  counts[N] = 1

  # 위상 정렬을 이용한다.
  queue = deque([x for x in range(1, N + 1) if not degrees[x]])

  while queue:
    node = queue.popleft()

    if not len(tree[node]) and counts[node]:
      result.append((node, counts[node]))

    for next, cost in tree[node]:
      counts[next] += counts[node] * cost
      degrees[next] -= 1

      if not degrees[next]:
        queue.append(next)

  result.sort()
  return result

if __name__ == '__main__':
  N, M = int(input()), int(input())
  tree = [set() for _ in range(N + 1)]
  degrees = [0] * (N + 1)

  for _ in range(M):
    x, y, k = map(int, input().split())
    tree[x].add((y, k))
    degrees[y] += 1

  results = solve(N, tree, degrees)

  for result in results:
    print(*result)
