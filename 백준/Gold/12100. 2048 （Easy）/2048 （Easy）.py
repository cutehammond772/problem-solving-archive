import sys
input = lambda: sys.stdin.readline().rstrip()

# LEFT, RIGHT, UP, DOWN
directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def copy(N, matrix):
  return [[matrix[row][col] for col in range(N)] for row in range(N)]

def largest(N, matrix):
  return max([max(matrix[row]) for row in range(N)])

def move(N, matrix, dir):
  result = copy(N, matrix)
  delta_row, delta_column = dir
  
  move_count = 0
  merge = set()
  
  for row in range(N)[::-(delta_row if delta_row != 0 else -1)]:
    for column in range(N)[::-(delta_column if delta_column != 0 else -1)]:
      if result[row][column] == 0:
        continue
        
      current_row = row
      current_column = column
      
      while True:
        next_row = current_row + delta_row
        next_column = current_column + delta_column
        
        if not (0 <= next_row < N and 0 <= next_column < N):
          break
            
        if result[next_row][next_column] > 0:
          # 서로 숫자가 같으면 합친다.
          if result[next_row][next_column] == result[current_row][current_column]:
            if (next_row, next_column) not in merge:
              result[next_row][next_column] *= 2
              result[current_row][current_column] = 0
              
              merge.add((next_row, next_column))
              move_count += 1
              
          break
        else:
          result[next_row][next_column] = result[current_row][current_column]
          result[current_row][current_column] = 0
          move_count += 1
            
        current_row = next_row
        current_column = next_column

  return result, move_count == 0
    
def solve(N, init):
  result = largest(N, init)
  
  def recursion(matrix, count):
    nonlocal result
    
    for dir in directions:
      next, same = move(N, matrix, dir)

      if not same:
        result = max(result, largest(N, next))
        
        if count < 4:
          recursion(next, count + 1)

  recursion(init, 0)
  return result

if __name__ == '__main__':
  N = int(input())
  matrix = []

  for _ in range(N):
    matrix.append([*map(int, input().split())])
    
  print(solve(N, matrix))