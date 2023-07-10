import sys
input = lambda: sys.stdin.readline().rstrip()

def calculate(N, X, Y):
  offset = 0
  result = [0] * (N * N)
  
  for p in range(N):
    for q in range(N):
      result[offset] = X[p] + Y[q]
      offset += 1

  result.sort()
  return result

def lb(A, K):
  x, y = 0, len(A)
  
  while x < y:
    mid = (x + y) // 2
    if A[mid] >= K:
      y = mid
    else:
      x = mid + 1
  
  return x

def ub(A, K):
  x, y = 0, len(A)
  
  while x < y:
    mid = (x + y) // 2
    if A[mid] > K:
      y = mid
    else:
      x = mid + 1
  
  return x - 1

def solve(N, A, B, C, D):
  result = 0

  P = calculate(N, A, B)
  Q = calculate(N, C, D)
  
  for idx in range(N * N):
    k = -P[idx]
    result += ub(Q, k) - lb(Q, k) + 1
  
  return result

if __name__ == '__main__':
  N = int(input())
  A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N
  
  for x in range(N):
    A[x], B[x], C[x], D[x] = map(int, input().split())

  print(solve(N, A, B, C, D))
