import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

SEA, LAND = 0, 1
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(N, matrix):
  visited = [[False] * N for _ in range(N)]
  ids = [[0] * N for _ in range(N)]
  count = [[0] * N for _ in range(N)]

  result = N * N
  traverse = deque([])
  
  # 1. 육지 구분
  curr_id = 0
  for row in range(N):
    for col in range(N):
      if visited[row][col] or matrix[row][col] == SEA:
        continue

      curr_id += 1
      queue = deque([(row, col)])
      
      ids[row][col] = curr_id
      visited[row][col] = True

      while queue:
        r, c = queue.popleft()
        for x in range(4):
          nr, nc = r + dr[x], c + dc[x]

          if not (0 <= nr < N and 0 <= nc < N):
            continue

          if visited[nr][nc]:
            continue

          ids[nr][nc] = curr_id
          visited[nr][nc] = True

          if matrix[nr][nc] == SEA:
            count[nr][nc] = 1
            traverse.append((nr, nc))
            continue
            
          queue.append((nr, nc))
          
  # 2. 최단거리 판단
  while traverse:
    row, col = traverse.popleft()
    
    if count[row][col] >= result:
      continue

    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      
      if not (0 <= nrow < N and 0 <= ncol < N):
        continue

      if visited[nrow][ncol]:
        if ids[nrow][ncol] != ids[row][col]:
          result = min(result, count[nrow][ncol] + count[row][col])
      else:
        ids[nrow][ncol] = ids[row][col]
        count[nrow][ncol] = count[row][col] + 1
        visited[nrow][ncol] = True

        traverse.append((nrow, ncol))

  return result

if __name__ == '__main__':
  N = int(input())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  print(solve(N, matrix))