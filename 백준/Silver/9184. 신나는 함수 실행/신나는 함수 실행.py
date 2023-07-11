import sys
input = lambda: sys.stdin.readline().strip()

def solver():
  memo = [[[0] * 21 for _ in range(21)] for _ in range(21)]

  # a, b, c = 0 ~ 21
  for x in range(21):
    for y in range(21):
      for z in range(21):
        # case 1
        if x == 0 or y == 0 or z == 0:
          memo[x][y][z] = 1
        # case 2
        elif x < y and y < z:
          memo[x][y][z] = memo[x][y][z - 1] + memo[x][y - 1][z - 1] - memo[x][y - 1][z]
        # case 3
        else:
          nx, ny, nz = max(0, x - 1), max(0, y - 1), max(0, z - 1)
          memo[x][y][z] = memo[nx][y][z] + memo[nx][ny][z] + memo[nx][y][nz] - memo[nx][ny][nz]
  
  def solve(a, b, c):
    # case 1
    if a <= 0 or b <= 0 or c <= 0:
      return 1
      
    # case 2
    if a > 20 or b > 20 or c > 20:
      return memo[20][20][20]
      
    return memo[a][b][c]
    
  return solve
  
if __name__ == '__main__':
  solve = solver()
  
  while True:
    a, b, c = map(int, input().split())
    
    # 종료
    if a == -1 and b == -1 and c == -1:
      break

    # 결과 출력
    print(f'w({a}, {b}, {c}) = {solve(a, b, c)}')