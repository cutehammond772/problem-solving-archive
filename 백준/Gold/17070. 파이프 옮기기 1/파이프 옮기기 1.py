import sys
input = lambda: sys.stdin.readline().rstrip()

FORWARD, CROSS, DOWN = 0, 1, 2

def cross_check(walls, row, col):
  return walls[row - 1][col - 1] != 1 and walls[row][col - 1] != 1 and walls[row - 1][col] != 1

def solve(walls, N):
  memo = [[[0] * 3 for _ in range(N)] for _ in range(N)]

  # 초기화
  memo[0][1][FORWARD] = 1
  
  # DP
  for x in range(2, N):
    # 1. 오른쪽 영역
    for t in range(x):
      if walls[t][x] == 1:
        continue
        
      if x != N - 1:
        memo[t][x][FORWARD] = memo[t][x - 1][FORWARD] + memo[t][x - 1][CROSS]

      if t > 0:
        if cross_check(walls, t, x):
          memo[t][x][CROSS] = sum(memo[t - 1][x - 1])
          
        memo[t][x][DOWN] = memo[t - 1][x][DOWN] + memo[t - 1][x][CROSS]
      
    # 2. 아래쪽 영역
    for t in range(x):
      if walls[x][t] == 1:
        continue
        
      if x != N - 1:   
        memo[x][t][DOWN] = memo[x - 1][t][DOWN] + memo[x - 1][t][CROSS]
        
      if t > 0:
        if cross_check(walls, x, t):
          memo[x][t][CROSS] = sum(memo[x - 1][t - 1])
          
        memo[x][t][FORWARD] = memo[x][t - 1][FORWARD] + memo[x][t - 1][CROSS]

    if walls[x][x] == 1:
      continue
      
    # 3-1. 왼쪽으로부터 FORWARD
    memo[x][x][FORWARD] = memo[x][x - 1][FORWARD] + memo[x][x - 1][CROSS]
    
    # 3-2. 아래로부터 DOWN
    memo[x][x][DOWN] = memo[x - 1][x][DOWN] + memo[x - 1][x][CROSS]
    
    # 3-3. 왼쪽 위로부터 CROSS
    if cross_check(walls, x, x):
      memo[x][x][CROSS] = sum(memo[x - 1][x - 1])

  return sum(memo[N - 1][N - 1])

if __name__ == '__main__':
  N = int(input())
  walls = [list(map(int, input().split())) for _ in range(N)]

  print(solve(walls, N))