import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 6 + 3

def mul(N, A, B):
  return [
    [
      sum(A[x][k] * B[k][y] for k in range(5 * N)) % MOD for y in range(5 * N)
    ] for x in range(5 * N)
  ]

def pow(N, matrix, T):
  result = [[1 if p == q else 0 for p in range(5 * N)] for q in range(5 * N)]

  while T:
    if T & 1:
      result = mul(N, result, matrix)

    T >>= 1
    matrix = mul(N, matrix, matrix)

  return result

def solve(N, S, E, T, matrix):
  result = pow(N, matrix, T)
  return result[5 * (S - 1)][5 * (E - 1)]

# 정점 분할 테크닉 이용
if __name__ == '__main__':
  N, S, E, T = map(int, input().split())
  matrix = [[0] * (5 * N) for _ in range(5 * N)]

  for row in range(N):
    data = [int(ch) for ch in input()]

    for col in range(N):
      node = data[col]

      for k in range(1, node):
        matrix[5 * row + (k - 1)][(5 * row) + k] = 1
      
      if node:
        matrix[(5 * row) + (node - 1)][5 * col] = 1

  print(solve(N, S, E, T, matrix))
