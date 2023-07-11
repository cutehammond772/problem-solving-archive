import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M):
  matrix = [[0] * N for _ in range(N)]
  
  def mul(i, j, k):
    return matrix[i][i + k] + matrix[i + (k + 1)][i + j] + (M[i] * M[i + k + 1] * M[i + j + 1])
  
  for j in range(N):
    for i in range(N - j):
      results = [mul(i, j, k) for k in range(j)]
      
      if results:
        matrix[i][i + j] = min(results)
      
  return matrix[0][N - 1]

if __name__ == '__main__':
  N = int(input())
  
  M = [0] * (N + 1)
  for x in range(N):
    A, B = map(int, input().split())
    M[x], M[x + 1] = A, B

  print(solve(N, M))