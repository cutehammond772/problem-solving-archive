import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
MAX = 2 ** 63 - 1

if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]
  H = int(input())

  total = [[MAX] * M for _ in range(N)]
  queue = deque([(0, 0, matrix[0][0])])
  total[0][0] = matrix[0][0]

  while queue:
    row, col, accu = queue.popleft()

    if accu > total[row][col] or accu > H:
      continue

    # 오른쪽으로 이동하는 경우
    if (col + 1) < M:
      if total[row][col + 1] > accu + matrix[row][col + 1]:
        total[row][col + 1] = accu + matrix[row][col + 1]
        queue.append((row, col + 1, total[row][col + 1]))

    # 아래쪽으로 이동하는 경우
    if (row + 1) < N:
      if total[row + 1][col] > accu + matrix[row + 1][col]:
        total[row + 1][col] = accu + matrix[row + 1][col]
        queue.append((row + 1, col, total[row + 1][col]))

  result = total[-1][-1]

  if result <= H:
    print("YES")
    print(result)
  else:
    print("NO")
