import sys
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

def solve(N, M, matrix, routes):
  U = [x for x in range(N + 1)]
  roots = set()

  for i in range(N - 1):
    for j in range(i + 1, N):
      if matrix[i][j]:
        union(U, i + 1, j + 1)

  for x in range(M):
    roots.add(find(U, routes[x]))

  return len(roots) == 1

if __name__ == "__main__":
  N, M = int(input()), int(input())
  matrix = [[*map(int, input().split())] for _ in range(N)]
  routes = [*map(int, input().split())]

  found = solve(N, M, matrix, routes)
  print("YES" if found else "NO")
