import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(N, M, matrix, start):
  result = [[-1] * M for _ in range(N)]

  # 원래 갈 수 없는 땅에 대한 전처리
  for row in range(N):
    for col in range(M):
      if matrix[row][col] == 0:
        result[row][col] = 0
        
  init_row, init_col = start
  queue = deque([(init_row, init_col, 0)])

  result[init_row][init_col] = 0

  while queue:
    row, col, dist = queue.popleft()
    
    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]

      if not (0 <= nrow < N and 0 <= ncol < M):
        continue

      if result[nrow][ncol] >= 0:
        continue

      result[nrow][ncol] = dist + 1
      queue.append((nrow, ncol, dist + 1))
      
  return result
  
if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [[0] * M for _ in range(N)]
  start = (-1, -1)
  
  for row in range(N):
    data = [*map(int, input().split())]
    
    for col in range(M):
      if data[col] == 2:
        start = (row, col)
        
      matrix[row][col] = data[col]
      
  result = solve(N, M, matrix, start)
  
  for row in range(N):
    print(*result[row])
  