import sys
input = lambda: sys.stdin.readline().rstrip()
INIT = 2 ** 100

def solve(N, M, matrix, start):
  P = [[0] * M for _ in range(N)]

  # 초기 설정
  P[0][start] = INIT

  for x in range(1, N):
    for col in range(M):
      if P[x - 1][col] == 0:
        continue

      if matrix[x][col] == 1:
        if (matrix[x - 1][col - 1] == 1 or matrix[x][col - 1] == 1) \
                and (matrix[x - 1][col + 1] == 1 or matrix[x][col + 1] == 1):
          continue

        if not (matrix[x - 1][col - 1] == 1 or matrix[x][col - 1] == 1):
          P[x][col - 1] += P[x - 1][col] // 2

        if not (matrix[x - 1][col + 1] == 1 or matrix[x][col + 1] == 1):
          P[x][col + 1] += P[x - 1][col] // 2
      else:
        P[x][col] += P[x - 1][col]

  return P[N - 1]

if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [[0] * M for _ in range(N)]

  for row in range(N):
    matrix[row] = [*map(int, input().split())]

  P = solve(N, M, matrix, matrix[0].index(2))
  V = max(P)

  if V == 0:
    print(-1)
  else:
    indexes = {x for x in range(M) if P[x] == V}
    print(min(indexes))
