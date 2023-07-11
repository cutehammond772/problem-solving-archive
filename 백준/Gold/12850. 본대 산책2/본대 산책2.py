import sys
input = lambda: sys.stdin.readline().rstrip()

matrix = [
  [0, 1, 1, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 0, 0, 0, 0],
  [1, 1, 0, 1, 1, 0, 0, 0],
  [0, 1, 1, 0, 1, 1, 0, 0],
  [0, 0, 1, 1, 0, 1, 1, 0],
  [0, 0, 0, 1, 1, 0, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 1],
  [0, 0, 0, 0, 0, 1, 1, 0]
]

def mul(N, M1, M2):
  matrix = [[0] * N for _ in range(N)]
  
  for x in range(N):
    for y in range(N):
      for k in range(N):
        matrix[x][y] += M1[x][k] * M2[k][y]
        
      matrix[x][y] %= 1000000007

  return matrix

if __name__ == '__main__':
  N = int(input())
  memo = [matrix]
  result = [[0 if x != y else 1 for y in range(8)] for x in range(8)]
  
  for x in range(1, 30):
    memo.append(mul(8, memo[-1], memo[-1]))

  for x in range(30):
    if N & (1 << x) > 0:
      result = mul(8, result, memo[x])
      
  print(result[0][0])