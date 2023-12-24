import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def convert(t):
  return int(t) - 1

if __name__ == "__main__":
  N, M = map(int, input().split())

  # 불이 켜진 방
  check = [[False] * N for _ in range(N)]

  # 방문 여부
  visited = [[False] * N for _ in range(N)]

  # 스위치
  switches = [[] for _ in range(N * N)]

  for _ in range(M):
    x, y, a, b = map(convert, input().split())
    switches[(x * N) + y].append((a, b))

  queue = deque([(0, 0)])

  # 시작 지점
  check[0][0] = True
  visited[0][0] = True

  while queue:
    x, y = queue.popleft()

    # 해당 스위치를 이용하여 불 켜기
    for a, b in switches[(x * N) + y]:
      check[a][b] = True

      if visited[a][b]:
        continue

      # 1. 불이 켜진 방 주위에 방문 가능한 방이 존재하면, 해당 (불이 켜진) 방 또한 방문 가능하다.
      adjacent = 0

      for i in range(4):
        na, nb = a + dx[i], b + dy[i]

        if not (0 <= na < N and 0 <= nb < N):
          continue

        adjacent += visited[na][nb]

      if adjacent:
        visited[a][b] = True
        queue.append((a, b))

    # 2. 방문한 방 주위에 불이 켜졌으나 방문하지 않은 방을 찾는다.
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if not (0 <= nx < N and 0 <= ny < N):
        continue

      if visited[nx][ny] or not check[nx][ny]:
        continue

      visited[nx][ny] = True
      queue.append((nx, ny))

  result = 0

  for x in range(N):
    for y in range(N):
      result += check[x][y]

  print(result)
