import sys
input = lambda: sys.stdin.readline().rstrip()

def check(area, x, k, W):
  first_row, second_row = area[0][x] + area[0][x - 1] <= W, area[1][x] + area[1][x - 1] <= W

  # [2, 2]
  if k == 0:
    return first_row and second_row

  # [1, 2]
  if k == 1:
    return second_row

  # [2, 1]
  if k == 2:
    return first_row

  # [1, 1]
  if k == 3:
    return True

  # [1열]
  if k == 4:
    return area[0][x] + area[1][x] <= W

  return False

def solve(N, W, area):
  INF = N * 2 + 1

  # N이 1인 경우
  if N == 1:
    if area[0][0] + area[1][0] <= W:
      return 1

    return 2

  # 첫 열과 마지막 열의 연관 관계는,
  # [2, 2], [1, 2], [2, 1], [1, 1], [1열]로 나뉜다.
  memo = [[[INF] * 5 for _ in range(N)] for _ in range(5)]

  # 연관 관계
  for t in range(5):
    if not check(area, 0, t, W):
      continue

    # 초기 설정
    memo[t][0][t] = 2 if t < 4 else 1

    # DP 수행
    for x in range(1, N - 1):
      for k in range(5):
        if not check(area, x, k, W):
          continue

        if k == 0:
          memo[t][x][k] = memo[t][x - 1][3]

        if k == 1:
          memo[t][x][k] = min(memo[t][x - 1][2], memo[t][x - 1][3]) + 1

        if k == 2:
          memo[t][x][k] = min(memo[t][x - 1][1], memo[t][x - 1][3]) + 1

        if k == 3:
          memo[t][x][k] = min(memo[t][x - 1]) + 2

        if k == 4:
          memo[t][x][k] = min(memo[t][x - 1]) + 1

    # 연관 관계에 따른 마지막 열의 처리
    if t == 0:
      memo[t][N - 1][3] = min(memo[t][N - 2])

    if t == 1:
      if check(area, N - 1, 2, W):
        memo[t][N - 1][2] = min(memo[t][N - 2][1], memo[t][N - 2][3])

      memo[t][N - 1][3] = min(memo[t][N - 2]) + 1

    if t == 2:
      if check(area, N - 1, 1, W):
        memo[t][N - 1][1] = min(memo[t][N - 2][2], memo[t][N - 2][3])

      memo[t][N - 1][3] = min(memo[t][N - 2]) + 1

    if t >= 3:
      if check(area, N - 1, 0, W):
        memo[t][N - 1][0] = memo[t][N - 2][3]

      if check(area, N - 1, 1, W):
        memo[t][N - 1][1] = min(memo[t][N - 2][2], memo[t][N - 2][3]) + 1

      if check(area, N - 1, 2, W):
        memo[t][N - 1][2] = min(memo[t][N - 2][1], memo[t][N - 2][3]) + 1

      if check(area, N - 1, 3, W):
        memo[t][N - 1][3] = min(memo[t][N - 2]) + 2

      if check(area, N - 1, 4, W):
        memo[t][N - 1][4] = min(memo[t][N - 2]) + 1

  return min([min(memo[x][N - 1]) for x in range(5)])

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N, W = map(int, input().split())
    area = [[*map(int, input().split())] for _ in range(2)]

    print(solve(N, W, area))
