import sys
input = lambda: sys.stdin.readline().rstrip()

RED, GREEN, BLUE = 0, 1, 2
NaN = 1000001
DIFF_COLORS = [[GREEN, BLUE], [RED, BLUE], [RED, GREEN]]

def solve(N, A):
  # [0][start][color]
  memo = [[[NaN] * 3 for _ in range(3)] for _ in range(N)]
  result = NaN
  
  for color in range(3):
    memo[0][color][color] = A[0][color]

  for x in range(1, N):
    for start in range(3):
      for color in range(3):
        memo[x][start][color] = min(
          [memo[x - 1][start][diff] for diff in DIFF_COLORS[color]]
        ) + A[x][color]

  for start in range(3):
    for diff in DIFF_COLORS[start]:
      result = min(result, memo[N - 1][start][diff])
      
  return result
  
if __name__ == '__main__':
  N = int(input())
  A = [list(map(int, input().split())) for _ in range(N)]

  print(solve(N, A))