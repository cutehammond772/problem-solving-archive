import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

INF = 10001
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

# 0-1 BFS 적용
def solve(N, M, matrix):
  # (row, col, count)
  queue = deque([(0, 0, 0)])
  
  # 최소 벽 개수
  memo = [[INF] * M for _ in range(N)]
  memo[0][0] = 0
  
  while queue:
    row, col, count = queue.popleft()
    
    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      
      if not (0 <= nrow < N and 0 <= ncol < M):
        continue
        
      weight = matrix[nrow][ncol]
      
      if weight == 0 and memo[nrow][ncol] > count:
        memo[nrow][ncol] = count
        queue.appendleft((nrow, ncol, count))
        
      if weight == 1 and memo[nrow][ncol] > count + 1:
        memo[nrow][ncol] = count + 1
        queue.append((nrow, ncol, count + 1))
        
  return memo[N - 1][M - 1]

if __name__ == '__main__':
  M, N = map(int, input().split())
  matrix = [[int(x) for x in input()] for _ in range(N)]
  
  print(solve(N, M, matrix))
  
  