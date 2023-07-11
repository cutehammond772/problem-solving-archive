import sys

input = lambda: sys.stdin.readline().rstrip()
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def find_purifier(matrix, N):
  for x in range(N - 1):
    if matrix[x][0] == -1:
      return x, x + 1
      
  return -1, -1

def total_dust(matrix, N, M):
  result = 0
  
  for row in range(N):
    for col in range(M):
      result += matrix[row][col]

  # 공기청정기의 (-1, -1)은 제외한다.
  return result + 2

def spread(matrix, N, M, purifier):
  # 확산된 먼지의 행렬이다.
  # 기존 행렬과 따로 분리하는 이유는, 확산된 먼지까지 같이 처리되는 것을 방지하기 위해서이다.
  addition = [[0] * M for _ in range(N)]
  
  for row in range(N):
    for col in range(M):
      dust = matrix[row][col]
      spreaded_dust = dust // 5
      
      if dust <= 0:
        continue
      
      for i in range(4):
        nrow, ncol = row + dr[i], col + dc[i]
        
        if not (0 <= nrow < N and 0 <= ncol < M):
          continue
          
        if ncol == 0:
          if nrow == purifier[0] or nrow == purifier[1]:
            continue
            
        addition[nrow][ncol] += spreaded_dust
        matrix[row][col] -= spreaded_dust

  # 다시 기존 행렬과 합친다.
  for row in range(N):
    for col in range(M):
      matrix[row][col] += addition[row][col]

def purify(matrix, N, M, purifier):
  top, bottom = purifier
  diff = [[-1] * M for _ in range(N)]
  
  # 윗부분 공기청정기 순환
  diff[top][1] = 0
  
  for x in range(M - 2):
    diff[top][2 + x] = matrix[top][1 + x]
    
  for x in range(top):
    diff[x][M - 1] = matrix[x + 1][M - 1]

  for x in range(M - 1):
    diff[0][x] = matrix[0][1 + x]

  for x in range(top - 1):
    diff[1 + x][0] = matrix[x][0]
    
  # 아랫부분 공기청정기
  diff[bottom][1] = 0
  
  for x in range(M - 2):
    diff[bottom][2 + x] = matrix[bottom][1 + x]
    
  for x in range(N - bottom - 1):
    diff[bottom + x + 1][M - 1] = matrix[bottom + x][M - 1]

  for x in range(M - 1):
    diff[N - 1][x] = matrix[N - 1][1 + x]
    
  for x in range(N - bottom - 2):
    diff[bottom + x + 1][0] = matrix[bottom + x + 2][0]
    
  # 기존 행렬에 적용
  for r in range(N):
    for c in range(M):
      if r <= top:
        if diff[r][c] != -1:
          matrix[r][c] = diff[r][c]
      elif r >= bottom:
        if diff[r][c] != -1:
          matrix[r][c] = diff[r][c]

if __name__ == '__main__':
  N, M, T = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(N)]
  purifier = find_purifier(matrix, N)

  # 확산 및 정화를 T번 반복한다.
  for _ in range(T):
    spread(matrix, N, M, purifier)
    purify(matrix, N, M, purifier)
  
  print(total_dust(matrix, N, M))
  