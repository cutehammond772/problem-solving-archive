import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(N, M, matrix):
  visited = [[False] * M for _ in range(N)]
  queue = deque()
  
  for row in range(N):
    for col in range(M):
      if visited[row][col]:
        continue
      
      color = matrix[row][col]
      
      visited[row][col] = True
      queue.append(((-1, -1), (row, col)))
      
      while queue:
        prev, curr = queue.popleft()
        
        for x in range(4):
          nrow, ncol = curr[0] + dr[x], curr[1] + dc[x]
          
          if (nrow, ncol) == prev:
            continue
          
          if not (0 <= nrow < N and 0 <= ncol < M):
            continue
          
          if matrix[nrow][ncol] != color:
            continue
          
          if visited[nrow][ncol]:
            return "Yes"
          
          visited[nrow][ncol] = True
          queue.append((curr, (nrow, ncol)))
  
  return "No"

if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [[*input()] for _ in range(N)]
  
  print(solve(N, M, matrix))
  