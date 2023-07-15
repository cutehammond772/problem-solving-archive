import sys
input = lambda: sys.stdin.readline().rstrip()
ROW_MEMO, COLUMN_MEMO, AREA_MEMO = 0, 1, 2

def convert(L):
  return ord(L[0]) - ord('A'), int(L[1]) - 1

def invalid(memo, row, col, num):
  if num in memo[ROW_MEMO][row]:
    return True
  
  if num in memo[COLUMN_MEMO][col]:
    return True
  
  if num in memo[AREA_MEMO][3 * (row // 3) + (col // 3)]:
    return True
  
  return False

def solve(matrix, dominos, memo):
  result = None
  
  def resolve_horizontal(row, col, left, right, offset):
    if invalid(memo, row, col, left) or invalid(memo, row, col + 1, right):
      return
      
    matrix[row][col] = left
    matrix[row][col + 1] = right
    dominos[left][right] = dominos[right][left] = True
    
    memo[ROW_MEMO][row].add(left)
    memo[ROW_MEMO][row].add(right)
    
    memo[COLUMN_MEMO][col].add(left)
    memo[COLUMN_MEMO][col + 1].add(right)
    
    memo[AREA_MEMO][3 * (row // 3) + (col // 3)].add(left)
    memo[AREA_MEMO][3 * (row // 3) + ((col + 1) // 3)].add(right)
    
    fill(offset + 1)
    
    matrix[row][col] = matrix[row][col + 1] = 0
    dominos[left][right] = dominos[right][left] = False
    
    memo[ROW_MEMO][row].remove(left)
    memo[ROW_MEMO][row].remove(right)
    
    memo[COLUMN_MEMO][col].remove(left)
    memo[COLUMN_MEMO][col + 1].remove(right)
    
    memo[AREA_MEMO][3 * (row // 3) + (col // 3)].remove(left)
    memo[AREA_MEMO][3 * (row // 3) + ((col + 1) // 3)].remove(right)
  
  def resolve_vertical(row, col, top, bottom, offset):
    if invalid(memo, row, col, top) or invalid(memo, row + 1, col, bottom):
      return
    
    matrix[row][col] = top
    matrix[row + 1][col] = bottom
    dominos[top][bottom] = dominos[bottom][top] = True
    
    memo[ROW_MEMO][row].add(top)
    memo[ROW_MEMO][row + 1].add(bottom)
    
    memo[COLUMN_MEMO][col].add(top)
    memo[COLUMN_MEMO][col].add(bottom)
    
    memo[AREA_MEMO][3 * (row // 3) + (col // 3)].add(top)
    memo[AREA_MEMO][3 * ((row + 1) // 3) + (col // 3)].add(bottom)
    
    fill(offset + 1)
    
    matrix[row][col] = matrix[row + 1][col] = 0
    dominos[top][bottom] = dominos[bottom][top] = False
    
    memo[ROW_MEMO][row].remove(top)
    memo[ROW_MEMO][row + 1].remove(bottom)
    
    memo[COLUMN_MEMO][col].remove(top)
    memo[COLUMN_MEMO][col].remove(bottom)
    
    memo[AREA_MEMO][3 * (row // 3) + (col // 3)].remove(top)
    memo[AREA_MEMO][3 * ((row + 1) // 3) + (col // 3)].remove(bottom)
  
  def fill(offset):
    nonlocal result
    
    if result:
      return
    
    if offset >= 81:
      result = [[matrix[row][col] for col in range(9)] for row in range(9)]
      return
    
    row, col = offset // 9, offset % 9
    
    if matrix[row][col]:
      fill(offset + 1)
      return
    
    # HORIZONTAL
    if col + 1 < 9 and not matrix[row][col + 1]:
      for left in range(1, 10):
        for right in range(left + 1, 10):
          # 도미노가 이미 배치된 경우
          if dominos[left][right] or dominos[right][left]:
            continue
          
          # [left, right]
          resolve_horizontal(row, col, left, right, offset)
          
          # [right, left]
          resolve_horizontal(row, col, right, left, offset)
    
    # VERTICAL
    if row + 1 < 9 and not matrix[row + 1][col]:
      for top in range(1, 10):
        for bottom in range(top + 1, 10):
          # 도미노가 이미 배치된 경우
          if dominos[top][bottom] or dominos[bottom][top]:
            continue
          
          # [top, bottom]
          resolve_vertical(row, col, top, bottom, offset)
          
          # [bottom, top]
          resolve_vertical(row, col, bottom, top, offset)
          
  fill(0)
  return result

if __name__ == '__main__':
  P = 0
  
  while N := int(input()):
    matrix = [[0] * 9 for _ in range(9)]
    dominos = [[False] * 10 for _ in range(10)]
    memo = [[set() for _ in range(9)] for _ in range(3)]
    
    for _ in range(N):
      U, LU, V, LV = input().split()
      U, V = int(U), int(V)
      
      ur, uc = convert(LU)
      matrix[ur][uc] = U
      memo[ROW_MEMO][ur].add(U)
      memo[COLUMN_MEMO][uc].add(U)
      memo[AREA_MEMO][3 * (ur // 3) + (uc // 3)].add(U)
      
      vr, vc = convert(LV)
      matrix[vr][vc] = V
      memo[ROW_MEMO][vr].add(V)
      memo[COLUMN_MEMO][vc].add(V)
      memo[AREA_MEMO][3 * (vr // 3) + (vc // 3)].add(V)
      
      dominos[U][V] = dominos[V][U] = True
    
    nums = [*map(convert, input().split())]
    
    for x in range(9):
      row, col = nums[x]
      num = matrix[row][col] = x + 1
      
      memo[ROW_MEMO][row].add(num)
      memo[COLUMN_MEMO][col].add(num)
      memo[AREA_MEMO][3 * (row // 3) + (col // 3)].add(num)
    
    result = solve(matrix, dominos, memo)
    
    print(f"Puzzle {(P := P + 1)}")
    
    for row in result:
      print(*row, sep='')
