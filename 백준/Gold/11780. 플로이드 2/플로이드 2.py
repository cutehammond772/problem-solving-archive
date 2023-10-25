import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10

if __name__ == "__main__":
  N, M = int(input()), int(input())

  adj = [[INF] * N for _ in range(N)]
  result = [[[] for _ in range(N)] for _ in range(N)]

  for x in range(N):
    adj[x][x] = 0

  for _ in range(M):
    x, y, k = map(int, input().split())

    adj[x - 1][y - 1] = min(adj[x - 1][y - 1], k)

  for x in range(N):
    for y in range(N):
      if 0 < adj[x][y] < INF:
        result[x][y] = [x + 1, y + 1]

  for k in range(N):
    for i in range(N):
      for j in range(N):
        dist = adj[i][k] + adj[k][j]

        if adj[i][j] > dist:
          adj[i][j] = dist
          result[i][j] = result[i][k][:-1] + result[k][j]

  for i in range(N):
    for j in range(N):
      if adj[i][j] == INF:
        adj[i][j] = 0

  for row in adj:
    print(*row)

  for i in range(N):
    for j in range(N):
      route = result[i][j]

      if not route:
        print(0)
      else:
        print(len(route), *route)
