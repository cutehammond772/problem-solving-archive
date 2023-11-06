import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def find(U, x):
  if U[x] == x:
    return U[x]

  routes = [x]

  while U[routes[-1]] != routes[-1]:
    routes.append(U[routes[-1]])

  for route in routes:
    U[route] = routes[-1]

  return U[x]

def union(U, x, y):
  x, y = find(U, x), find(U, y)

  if x <= y:
    U[y] = x
  else:
    U[x] = y

# MST 이용
def solve(N, flow):
  group = [x for x in range(N)]
  result = 0

  count = N - 1
  edges = []

  for x in range(N - 1):
    for y in range(x + 1, N):
      heappush(edges, (flow[x][y], x, y))

  while count:
    cost, x, y = heappop(edges)

    if find(group, x) == find(group, y):
      continue

    union(group, x, y)
    result += cost
    count -= 1

  return result

if __name__ == "__main__":
  N = int(input())
  flow = [[*map(int, input().split())] for _ in range(N)]

  print(solve(N, flow))
