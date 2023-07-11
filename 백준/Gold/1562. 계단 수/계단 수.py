import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  memo = [[[0] * 1024 for _ in range(10)] for _ in range(N)]

  # 시작하는 수는 0이 될 수 없다.
  for x in range(1, 10):
    memo[0][x][1 << x] = 1
    
  for x in range(1, N):
    for y in range(10):
      for k in range(1024):
        idx = k | 1 << y
        
        if y > 0:
          memo[x][y][idx] += memo[x - 1][y - 1][k]
          
        if y < 9:
          memo[x][y][idx] += memo[x - 1][y + 1][k]
        
        memo[x][y][idx] %= 10 ** 9

  
  print(sum([memo[N - 1][x][1023] for x in range(10)]) % 10 ** 9)