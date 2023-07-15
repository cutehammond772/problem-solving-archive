import sys
input = lambda: sys.stdin.readline().rstrip()
ROW_MEMO, COLUMN_MEMO, AREA_MEMO = 0, 1, 2
  
def solve(matrix, memo, init):
  result = None
  
  def fill(offset):
    nonlocal result
    
    if result:
      return
    
    if offset == 81:
      result = [[matrix[row][col] for col in range(9)] for row in range(9)]
      return
    
    row, col = offset // 9, offset % 9
      
    if init[row][col]:
      fill(offset + 1)
      return
        
    for num in range(1, 10):
      if num in memo[ROW_MEMO][row]:
        continue
      
      if num in memo[COLUMN_MEMO][col]:
        continue
      
      if num in memo[AREA_MEMO][3 * (row // 3) + (col // 3)]:
        continue
          
      matrix[row][col] = num
      memo[ROW_MEMO][row].add(num)
      memo[COLUMN_MEMO][col].add(num)
      memo[AREA_MEMO][3 * (row // 3) + (col // 3)].add(num)
      
      fill(offset + 1)
      
      matrix[row][col] = 0
      memo[ROW_MEMO][row].remove(num)
      memo[COLUMN_MEMO][col].remove(num)
      memo[AREA_MEMO][3 * (row // 3) + (col // 3)].remove(num)
  
  fill(0)
  return result

if __name__ == '__main__':
  matrix = []
  memo = [[set() for _ in range(9)] for _ in range(3)]
  init = [[False] * 9 for _ in range(9)]
  
  for row in range(9):
    data = [*map(int, input().split())]
    matrix.append(data)
    
    for col in range(9):
      num = data[col]
      
      if num == 0:
        continue
      
      init[row][col] = True
      memo[ROW_MEMO][row].add(num)
      memo[COLUMN_MEMO][col].add(num)
      memo[AREA_MEMO][3 * (row // 3) + (col // 3)].add(num)
    
  result = solve(matrix, memo, init)
  
  for row in result:
    print(*row)
  