import sys
input = lambda: sys.stdin.readline().rstrip()
BLANK, WALL, CLEANED = 0, 1, 2

# 방향 (북 -> 동 -> 남 -> 서)
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def solve(room, initial_state):
  row, col, dir = initial_state

  # 청소하는 칸의 개수
  result = 0

  def adjacent_blanks():
    blank_count = 0

    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      blank_count += room[nrow][ncol] == BLANK

    return blank_count

  while True:
    # 1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
    if room[row][col] == BLANK:
      room[row][col] = CLEANED
      result += 1

    adjacent = adjacent_blanks()

    # 2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
    if adjacent == 0:
      back = (dir + 2) % 4
      nrow, ncol = row + dr[back], col + dc[back]

      # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
      if room[nrow][ncol] == WALL:
        break

      # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
      row, col = nrow, ncol

    # 3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
    if adjacent > 0:
      # 반시계 방향으로 90도 회전한다.
      dir = (dir - 1) % 4
      nrow, ncol = row + dr[dir], col + dc[dir]

      # 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
      if room[nrow][ncol] == BLANK:
        row, col = nrow, ncol

  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  r, c, d = map(int, input().split())

  room = [[*map(int, input().split())] for _ in range(N)]

  print(solve(room, (r, c, d)))
