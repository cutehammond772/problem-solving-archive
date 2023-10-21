import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

INF = 10 ** 10
target = 2271560481
mask = (1 << 36) - 1

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def possible():
  memo = {}

  # (가능한 경우의 수를 판단하기 위해) 끝 지점에서부터 시작한다.
  memo[target] = 0
  queue = deque([(target, 8, 0)])

  while queue:
    status, current, count = queue.popleft()
    row, col = current // 3, current % 3

    if memo[status] < count:
      continue

    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      next = nrow * 3 + ncol

      # 다음 위치에 대한 유효성 체크
      if not (0 <= nrow < 3 and 0 <= ncol < 3):
        continue

      # 다음 위치 구하기
      next_num = (status & (15 << (4 * next))) >> (4 * next)
      next_status = (status | (next_num << (4 * current))) & (mask ^ (15 << (4 * next)))

      if next_status in memo and memo[next_status] <= count + 1:
        continue

      memo[next_status] = count + 1
      queue.append((next_status, next, count + 1))

  return memo

# 시작 지점을 고유 값으로 변환
def get_data():
  data = [0] * 9

  for off in range(0, 9, 3):
    data[off:off + 3] = [int(x) for x in input().replace('#', '0')]

  pos = 0

  for i in range(9):
    pos |= data[i] << (4 * i)

  return pos

if __name__ == "__main__":
  T = int(input())
  memo = possible()

  for _ in range(T):
    # 빈칸 넘기기
    input()

    # 시작 지점 가져오기
    pos = get_data()

    if pos in memo: print(memo[pos])
    else: print("impossible")
