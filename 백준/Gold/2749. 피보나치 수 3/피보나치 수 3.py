import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 6

def mul(x, y):
  return [
    [(x[0][0] * y[0][0] + x[0][1] * y[1][0]) % MOD, (x[0][0] * y[0][1] + x[0][1] * y[1][1]) % MOD],
    [(x[1][0] * y[0][0] + x[1][1] * y[1][0]) % MOD, (x[1][0] * y[0][1] + x[1][1] * y[1][1]) % MOD]
  ]

def solve(N):
  result = [[1, 0], [0, 1]]
  matrix = [[1, 1], [1, 0]]

  while N:
    if N & 1:
      result = mul(result, matrix)

    matrix = mul(matrix, matrix)
    N >>= 1

  return result[1][0]

if __name__ == "__main__":
  N = int(input())
  print(solve(N))