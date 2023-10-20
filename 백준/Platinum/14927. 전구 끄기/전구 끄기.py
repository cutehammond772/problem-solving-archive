import sys
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [0, 0, 1, 0, -1], [0, 1, 0, -1, 0]
INF = 325

# 특정 위치를 지나갈 때, 바로 윗 열이 0이 되도록 해야 한다.
# 즉, 행 단위로 윗 행이 모두 0이 되도록 불을 꺼주면 된다.
# 이때, 첫 행의 경우의 수만 따지면 그 이후의 행은 한 가지 경우밖에 존재하지 않는다.
def solve(N, matrix):
  result = INF

  def toggle(row, batch):
    for col in range(N):
      if not batch & 1 << col:
        continue

      for x in range(5):
        nrow, ncol = row + dr[x], col + dc[x]

        if not (0 <= nrow < N and 0 <= ncol < N):
          continue

        matrix[nrow] ^= 1 << ncol

  def count(x):
    result = 0

    while x:
      if x & 1:
        result += 1

      x >>= 1

    return result

  def check(row, count):
    nonlocal result

    if count >= result:
      return

    if row >= N:
      if matrix[-1] == 0:
        result = min(result, count)

      return

    batch, extra = 0, 0

    for col in range(N):
      if matrix[row - 1] & 1 << col:
        batch |= 1 << col
        extra += 1

    toggle(row, batch)
    check(row + 1, count + extra)
    toggle(row, batch)

  for first in range(1 << N):
    toggle(0, first)
    check(1, count(first))
    toggle(0, first)

  return -1 if result == INF else result

def convert(*S):
  result = 0

  for i in range(len(S)):
    result |= S[i] << i

  return result

if __name__ == "__main__":
  N = int(input())
  matrix = [convert(*map(int, input().split())) for _ in range(N)]

  print(solve(N, matrix))
