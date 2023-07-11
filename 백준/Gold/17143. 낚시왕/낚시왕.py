import sys
input = lambda: sys.stdin.readline().rstrip()

UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4

# 방향 값
directions = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]

# 반대 방향
opposites = [0, DOWN, UP, LEFT, RIGHT]

def hunt(R, C, matrix, phase):
  for idx in range(R):
    if matrix[idx][phase] >= 0:
      return idx
      
  return -1

def resolve(x, k, bound):
  # 범위 내에 존재하는 경우
  if 0 <= x + k < bound:
    return x + k, False

  # 음의 방향으로 오버플로우
  if x + k < 0:
    order = (x + k) // (bound - 1)
    
    if order % 2 == 0:
      idx = (x + k) % (bound - 1)
    else:
      idx = (bound - 1) - (x + k) % (bound - 1)
    
    return idx, order % 2 == 1
  
  # 양의 방향으로 오버플로우
  order = (x + k - 1) // (bound - 1)
  
  if order % 2 == 0:
    idx = 1 + (x + k - 1) % (bound - 1)
  else:
    idx = (bound - 2) - (x + k - 1) % (bound - 1)
  
  return idx, order % 2 == 1

def move(R, C, sharks, matrix):
  result = [[-1] * C for _ in range(R)]
  
  for row in range(R):
    for col in range(C):
      shark = matrix[row][col]
      
      if shark < 0:
        continue

      speed, dir, size = sharks[shark]
      dr, dc = directions[dir]

      nrow, dr_change = resolve(row, speed * dr, R)
      ncol, dc_change = resolve(col, speed * dc, C)

      if result[nrow][ncol] >= 0:
        if sharks[result[nrow][ncol]][2] > size:
          continue
            
      # 방향이 바뀌는 경우 (성립해도 무조건 둘 중 하나만 성립한다.)
      if dr_change or dc_change:
        sharks[shark][1] = opposites[dir]
          
      result[nrow][ncol] = shark
        
  return result

def solve(R, C, M, sharks, matrix):
  result = 0
  
  # 상어의 수가 0일 경우
  if M == 0:
    return result
  
  # 한 페이즈: 낚시왕 이동 -> 사냥 -> 상어 이동
  for phase in range(C):
    # 2. 사냥
    shark_idx = hunt(R, C, matrix, phase)

    # 사냥할 상어가 존재하는 경우
    if shark_idx >= 0:
      result += sharks[matrix[shark_idx][phase]][2]
      matrix[shark_idx][phase] = -1
  
    # 3. 상어 이동
    if phase == C - 1:
      break

    matrix = move(R, C, sharks, matrix)
    
  return result

def preprocess(R, C, M):
  matrix = [[-1] * C for _ in range(R)]
  sharks = []

  for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    
    matrix[r - 1][c - 1] = len(sharks)
    sharks.append([s, d, z])
    
  return sharks, matrix

if __name__ == '__main__':
  R, C, M = map(int, input().split())
  sharks, matrix = preprocess(R, C, M)

  print(solve(R, C, M, sharks, matrix))