import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# UP, DOWN, LEFT, RIGHT
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def marker(N, M, walls):
  mask = [[-1] * M for _ in range(N)]
  area = []
  
  def mark(init_row, init_col):
    if mask[init_row][init_col] >= 0:
      return mask[init_row][init_col], area[mask[init_row][init_col]]

    idx = len(area)
    area.append(0)
    
    queue = deque([(init_row, init_col, idx)])
    mask[init_row][init_col] = idx
    area[idx] += 1
    
    while queue:
      row, col, idx = queue.popleft()

      for d in directions:
        nrow, ncol = row + d[0], col + d[1]
        
        if not (0 <= nrow < N and 0 <= ncol < M):
          continue

        if (nrow, ncol) in walls:
          continue

        if mask[nrow][ncol] >= 0:
          continue

        mask[nrow][ncol] = idx
        area[idx] += 1
        
        queue.append((nrow, ncol, idx))

    return idx, area[idx]
    
  return mark
        
def solve(N, M, matrix, walls):
  mark = marker(N, M, walls)
  
  for row, col in walls:
    area = set()
    
    for d in directions:
      nrow, ncol = row + d[0], col + d[1]
      
      if not (0 <= nrow < N and 0 <= ncol < M):
        continue

      if (nrow, ncol) in walls:
        continue

      idx, count = mark(nrow, ncol)
      
      if idx not in area:
        matrix[row][col] = (matrix[row][col] + count) % 10
        area.add(idx)
        
def preprocess(N, M):
  matrix = [[0] * M for _ in range(N)]
  walls = set()
  
  for row in range(N):
    raw_data = input()
    
    for col in range(M):
      if raw_data[col] == '1':
        walls.add((row, col))
        matrix[row][col] = 1
        
  return matrix, walls

def visualize(matrix):
  for row in matrix:
    print(*row, sep = '')

if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix, walls = preprocess(N, M)
  
  solve(N, M, matrix, walls)
  visualize(matrix)