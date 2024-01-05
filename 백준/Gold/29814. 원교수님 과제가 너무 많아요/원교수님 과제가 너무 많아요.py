import sys
from heapq import heapify, heappop
input = lambda: sys.stdin.readline().rstrip()

def union(U, x, y):
  x, y = find(U, x), find(U, y)

  if U[x] < U[y]:
    U[y] = U[x]
  else:
    U[x] = U[y]

def find(U, x):
  if U[x] == x:
    return x

  routes = [x]

  while U[routes[-1]] != routes[-1]:
    routes.append(U[routes[-1]])

  for node in routes:
    U[node] = routes[-1]

  return U[x]

def solve(N, C, heap):
  heapify(heap)

  U = [*range(N + 1)]
  count, points = 0, 0

  while heap and points < C:
    point, last = heappop(heap)

    if find(U, last) == 0:
      continue

    union(U, U[last], U[last] - 1)

    points += -point
    count += 1

  if points < C:
    return "I'm sorry professor Won!"

  return count

if __name__ == '__main__':
  N, C = map(int, input().split())
  A = []

  for _ in range(N):
    d, t, p = map(int, input().split())

    # (포인트, 시작일 커트라인)
    A.append((-p, d - t + 1))

  print(solve(N, C, A))
