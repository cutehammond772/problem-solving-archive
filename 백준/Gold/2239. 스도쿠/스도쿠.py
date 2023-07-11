import sys
input = lambda: sys.stdin.readline().rstrip()

MAX = 405

def square_idx(row, col):
  return (row // 3) * 3 + (col // 3)

def copy(matrix):
  result = [[0] * 9 for _ in range(9)]
  
  for row in range(9):
    for col in range(9):
      result[row][col] = matrix[row][col]

  return result

def solve(matrix):
  rows, cols, squares = preprocess(matrix)

  result = [[9] * 9 for _ in range(9)]
  
  def invalid(row, col, K):
    row_check = (rows[row] & (1 << K)) > 0
    col_check = (cols[col] & (1 << K)) > 0
    square_check = (squares[square_idx(row, col)] & (1 << K)) > 0
    
    return row_check or col_check or square_check

  def mark(row, col, K):
    nonlocal matrix, rows, cols, squares
    
    matrix[row][col] = K
    
    rows[row] |= 1 << K
    cols[col] |= 1 << K
    squares[square_idx(row, col)] |= 1 << K

  def unmark(row, col, K):
    nonlocal matrix, rows, cols, squares
    
    matrix[row][col] = 0
    
    rows[row] ^= 1 << K
    cols[col] ^= 1 << K
    squares[square_idx(row, col)] ^= 1 << K

  def next_idx(row, col):
    next = row * 9 + col + 1
    
    while next // 9 < 9 and matrix[next // 9][next % 9] > 0:
      next += 1
      
    return next // 9, next % 9
  
  def recursion(row, col):
    nonlocal result

    if matrix[row][col] > 0:
      nrow, ncol = next_idx(row, col)
      recursion(nrow, ncol)
      return
      
    for x in range(1, 10):
      if not invalid(row, col, x):
        if result[row][col] < x:
          break

        mark(row, col, x)
        
        nrow, ncol = next_idx(row, col)

        if nrow == 9:
          result = copy(matrix)
        else:
          recursion(nrow, ncol)
          
        unmark(row, col, x)

  recursion(0, 0)
  return result

def preprocess(matrix):
  rows, cols, squares = [0] * 9, [0] * 9, [0] * 9

  for row in range(9):
    for col in range(9):
      if matrix[row][col] > 0:
        rows[row] |= 1 << matrix[row][col]
        cols[col] |= 1 << matrix[row][col]
        squares[square_idx(row, col)] |= 1 << matrix[row][col]
        
  return rows, cols, squares

if __name__ == '__main__':
  matrix = [[int(ch) for ch in input()] for _ in range(9)]
  
  for row in solve(matrix):
    print(*row, sep = '')