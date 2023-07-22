import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

CLE, FUR, DIR = 0, 1, 2
convert = {'.': CLE, 'x': FUR, '*': DIR, 'o': CLE}

dr, dc = [0, -1, 0, 1], [-1, 0, 1, 0]
INF = 10001

def analyse(N, M):
  matrix = [[0] * M for _ in range(N)]
  start_point = None
  dirty_points = []

  for row in range(N):
    data = input()

    for col in range(M):
      if data[col] == 'o':
        start_point = (row, col)

      elif data[col] == '*':
        dirty_points.append((row, col))

      matrix[row][col] = convert[data[col]]

  return matrix, start_point, dirty_points

# 두 점 간의 최단 거리 찾기
def distance(N, M, matrix, P, Q):
  visited = [[False] * M for _ in range(N)]
  rp, cp = P
  rq, cq = Q

  queue = deque([(rp, cp, 0)])
  visited[rp][cp] = True

  while queue:
    row, col, dist = queue.popleft()

    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      next_dist = dist + 1

      if not (0 <= nrow < N and 0 <= ncol < M):
        continue

      if visited[nrow][ncol] or matrix[nrow][ncol] == FUR:
        continue

      if nrow == rq and ncol == cq:
        return next_dist

      visited[nrow][ncol] = True
      queue.append((nrow, ncol, next_dist))

  return INF

def solve(N, M, matrix, start, dirties):
  result = INF
  D = len(dirties)

  P = [*range(D)]
  distances = [[INF] * (N * M) for _ in range(N * M)]

  # 두 점 간의 거리 메모
  for x in range(D):
    dx = dirties[x]
    dist = distance(N, M, matrix, start, dx)
    distances[start[0] * M + start[1]][dx[0] * M + dx[1]] = dist

  for x in range(D - 1):
    for y in range(x + 1, D):
      dx, dy = dirties[x], dirties[y]
      dist = distance(N, M, matrix, dx, dy)

      distances[dx[0] * M + dx[1]][dy[0] * M + dy[1]] = dist
      distances[dy[0] * M + dy[1]][dx[0] * M + dx[1]] = dist

  # 순열을 스왑으로 구현 => O(N!)
  def recursion(count):
    nonlocal result

    if count == D:
      total = distances[start[0] * M + start[1]][dirties[P[0]][0] * M + dirties[P[0]][1]]

      for x in range(1, D):
        total += distances[
          dirties[P[x - 1]][0] * M + dirties[P[x - 1]][1]
        ][
          dirties[P[x]][0] * M + dirties[P[x]][1]
        ]

      result = min(result, total)
      return

    for x in range(count, D):
      P[x], P[count] = P[count], P[x]
      recursion(count + 1)
      P[x], P[count] = P[count], P[x]

  recursion(0)
  return result

if __name__ == '__main__':
  while True:
    M, N = map(int, input().split())

    if M == N == 0:
      break

    matrix, start, dirties = analyse(N, M)
    result = solve(N, M, matrix, start, dirties)
    print(-1 if result == INF else result)
