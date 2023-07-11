import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

convert = { 'O': 0, 'I': 0, 'X': 1, 'P': 2 }
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(N, M, loc, matrix):
  result = 0
  visited = [[False] * M for _ in range(N)]
  
  queue = deque([loc])
  visited[loc[0]][loc[1]] = True
  
  while queue:
    row, col = queue.popleft()
    
    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      
      if not (0 <= nrow < N and 0 <= ncol < M):
        continue

      if visited[nrow][ncol] or matrix[nrow][ncol] == 1:
        continue

      if matrix[nrow][ncol] == 2:
        result += 1
        
      visited[nrow][ncol] = True
      queue.append((nrow, ncol))
      
  return result
      

def preprocess(N, M):
  matrix = [[0] * M for _ in range(N)]
  loc = (-1, -1)
  
  for row in range(N):
    data = input()
    
    for col in range(M):
      matrix[row][col] = convert[data[col]]

      if data[col] == 'I':
        loc = (row, col)
        
  return loc, matrix

if __name__ == '__main__':
  N, M = map(int, input().split())
  loc, matrix = preprocess(N, M)

  result = solve(N, M, loc, matrix)
  print("TT" if result == 0 else result)
  