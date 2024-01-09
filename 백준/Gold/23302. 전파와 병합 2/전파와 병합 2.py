import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

ch_A, ch_Z = ord('A'), ord('Z')
ch_0, ch_9 = ord('0'), ord('9')

def convert(name):
  row, col = 0, 0

  for ch in name:
    ch = ord(ch)

    if ch_0 <= ch <= ch_9:
      row = (row * 10) + (ch - ch_0)

    if ch_A <= ch <= ch_Z:
      col = (col * 26) + (ch - ch_A + 1)

  return row, col

def solve(R, C, reference_graph, reference_count):
  queue = deque([])
  nodes = R * C

  for row in range(1, R + 1):
    for col in range(1, C + 1):
      if reference_count[row][col] == 0:
        queue.append((row, col))

  while queue:
    row, col = queue.popleft()
    nodes -= 1

    for nrow, ncol in reference_graph[row][col]:
      reference_count[nrow][ncol] -= 1

      if reference_count[nrow][ncol] == 0:
        queue.append((nrow, ncol))

  return nodes > 0

if __name__ == '__main__':
  R, C = map(int, input().split())

  reference_graph = [[[] for _ in range(C + 1)] for _ in range(R + 1)]
  reference_count = [[0] * (C + 1) for _ in range(R + 1)]

  for row in range(1, R + 1):
    data = input().split()

    for col in range(1, C + 1):
      # 어떤 셀도 참조하지 않는 경우
      if data[col - 1] == '.':
        continue

      references = data[col - 1].split("+")

      for reference in references:
        nrow, ncol = convert(reference)

        reference_graph[nrow][ncol].append((row, col))
        reference_count[row][col] += 1

  has_cycle = solve(R, C, reference_graph, reference_count)
  print("yes" if has_cycle else "no")
