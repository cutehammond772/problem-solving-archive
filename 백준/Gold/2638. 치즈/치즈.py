import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(matrix, N, M):
  hour = 0
  cheese = sum([matrix[r][c] for c in range(M) for r in range(N)])
  visited = [[False] * M for _ in range(N)]
  
  queue = deque()
  queue.append((0, 0))
  visited[0][0] = True
  
  while cheese != 0:
    while queue:
      row, col = queue.popleft()
      
      for i in range(4):
        nrow, ncol = row + dr[i], col + dc[i]
        
        if not (0 <= nrow < N and 0 <= ncol < M):
          continue
          
        if matrix[nrow][ncol] >= 1:
          matrix[nrow][ncol] += 1
        elif not visited[nrow][ncol]:
          queue.append((nrow, ncol))
          visited[nrow][ncol] = True

    for row in range(N):
      for col in range(M):
        if matrix[row][col] > 2:
          matrix[row][col] = 0
          cheese -= 1
          queue.append((row, col))
          visited[row][col] = True
          
    hour += 1
    
  return hour
        
if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(N)]
  
  print(solve(matrix, N, M))