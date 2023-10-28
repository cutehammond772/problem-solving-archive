import sys, time
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

target = 87654321
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

# 더 빠른 수행을 위한 전처리
tens = [10 ** x for x in range(10)]
pp = [[[0] * 9 for _ in range(9)] for _ in range(9)]

for a in range(9):
  for x in range(9):
    for y in range(9):
      pp[a][x][y] = a * (tens[x] - tens[y])

def possible():
  memo = {}

  # (가능한 경우의 수를 판단하기 위해) 끝 지점에서부터 시작한다.
  memo[target] = 0
  queue = deque([(target, 8, 0)])

  while queue:
    status, current, count = queue.popleft()
    row, col = current // 3, current % 3

    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      next = nrow * 3 + ncol

      # 다음 위치에 대한 유효성 체크
      if not (0 <= nrow < 3 and 0 <= ncol < 3):
        continue

      # 다음 위치 구하기
      next_num = (status // tens[next]) % 10
      next_status = status + pp[next_num][current][next]

      if next_status in memo:
        continue

      memo[next_status] = count + 1
      queue.append((next_status, next, count + 1))

  return memo

# 시작 지점을 고유 값으로 변환
def get_data():
  data = ''

  for _ in range(3):
    data += input().replace('#', '0')

  return int(data[::-1])

if __name__ == "__main__":
  T = int(input())
  memo = possible()

  for _ in range(T):
    # 빈칸 넘기기
    input()

    # 시작 지점 가져오기
    pos = get_data()

    if pos in memo:
      print(memo[pos])
    else:
      print("impossible")
