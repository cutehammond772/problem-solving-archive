import sys
from queue import Queue
input = lambda: sys.stdin.readline().strip()

MAX_DIST = 1000000
PATH, WALL = 0, 1

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(maze, N, M):
  # 벽을 부수지 않았을 경우
  dist = [[MAX_DIST] * M for _ in range(N)]
  # 벽을 부쉈을 경우
  b_dist = [[MAX_DIST] * M for _ in range(N)]
  
  que = Queue()
  
  # (row, col, 벽을 부순 여부)
  que.put((0, 0, False))
  dist[0][0] = 1
  
  while not que.empty():
    row, col, broken = que.get()
    
    # 벽을 부수지 않았을 경우
    if not broken:
      for i in range(4):
        nrow, ncol = row + dr[i], col + dc[i]
        
        if not ((0 <= nrow < N) and (0 <= ncol < M)):
          continue
          
        if dist[nrow][ncol] > dist[row][col] + 1:
          dist[nrow][ncol] = dist[row][col] + 1
          
          if maze[nrow][ncol] == WALL:
            que.put((nrow, ncol, True))
            b_dist[nrow][ncol] = dist[nrow][ncol]
          else:
            que.put((nrow, ncol, False))
            
    # 벽을 부쉈을 경우      
    else:
      for i in range(4):
        nrow, ncol = row + dr[i], col + dc[i]
        
        if not ((0 <= nrow < N) and (0 <= ncol < M)):
          continue
          
        if maze[nrow][ncol] == WALL:
          continue
          
        if b_dist[nrow][ncol] > b_dist[row][col] + 1:
          b_dist[nrow][ncol] = b_dist[row][col] + 1
          que.put((nrow, ncol, True))

  result = min(dist[N - 1][M - 1], b_dist[N - 1][M - 1])
  return result if result != MAX_DIST else -1
      
          
if __name__ == '__main__':
  N, M = map(int, input().split())
  maze = [[int(chr) for chr in input()] for _ in range(N)]
  
  result = solve(maze, N, M)
  print(result)