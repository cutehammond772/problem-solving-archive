import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, blocks, offset):
  result = 0
  bishops = [[False] * N for _ in range(N)]

  def first(row):
    return offset if row % 2 == 0 else (1 - offset)

  def invalid(row, col):
    if blocks[row][col]:
      return True

    for x in range(row):
      lcol, rcol = col - (row - x), col + (row - x)
      
      if lcol >= 0 and bishops[x][lcol]:
        return True
        
      if rcol < N and bishops[x][rcol]:
        return True
        
    return False
  
  def recursion(row_off, col_off, count):
    nonlocal result
    
    for row in range(row_off, N):
      for col in range(first(row), N, 2):
        if row == row_off and col < col_off:
          continue
          
        if invalid(row, col):
          continue

        bishops[row][col] = True
        recursion(row, col + 2, count + 1)
        bishops[row][col] = False
        
    result = max(result, count)

  recursion(0, offset, 0)
  return result

def convert(x):
  return int(x) == 0

if __name__ == '__main__':
  N = int(input())
  blocks = [[*map(convert, input().split())] for _ in range(N)]

  print(solve(N, blocks, 0) + solve(N, blocks, 1))