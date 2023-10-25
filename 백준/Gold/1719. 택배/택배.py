import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 200000

if __name__ == "__main__":
  N, M = map(int, input().split())

  adj = [[INF] * N for _ in range(N)]
  result = [[[] for _ in range(N)] for _ in range(N)]

  for x in range(N):
    adj[x][x] = 0

  for _ in range(M):
    x, y, k = map(int, input().split())
    adj[x - 1][y - 1] = adj[y - 1][x - 1] = k

    result[x - 1][y - 1].append(y)
    result[y - 1][x - 1].append(x)

  for k in range(N):
    for i in range(N):
      for j in range(N):
        dist = adj[i][k] + adj[k][j]

        if adj[i][j] > dist:
          adj[i][j] = dist
          result[i][j] = result[i][k] + result[k][j]

  for i in range(N):
    row = []

    for j in range(N):
      if not result[i][j]: row.append('-')
      else: row.append(result[i][j][0])

    print(*row)
