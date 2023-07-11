import sys
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(N, M, K, matrix):
  result = -10000001
  marked = [[0] * M for _ in range(N)]
  
  def mark(row, col, mark=True):
    delta = 1 if mark else -1
    
    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]
      
      if not (0 <= nrow < N and 0 <= ncol < M):
        continue
        
      marked[nrow][ncol] += delta
  
  def traverse(offset, count, accu):
    nonlocal result
    
    if count == K:
      result = max(result, accu)
      return
    
    for next in range(offset, N * M):
      row, col = next // M, next % M
      
      if marked[row][col] > 0:
        continue
        
      mark(row, col)
      traverse(next + 1, count + 1, accu + matrix[row][col])
      mark(row, col, False)
  
  traverse(0, 0, 0)
  return result

if __name__ == '__main__':
  N, M, K = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]
  
  print(solve(N, M, K, matrix))
  