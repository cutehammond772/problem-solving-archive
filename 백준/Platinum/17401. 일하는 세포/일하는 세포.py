import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

def default_matrix():
  return [[1 if p == q else 0 for p in range(N)] for q in range(N)]

def multiply(N, A, B):
  result = [[0] * N for _ in range(N)]

  for x in range(N):
    for y in range(N):
      for k in range(N):
        result[x][y] = (result[x][y] + A[x][k] * B[k][y]) % MOD

  return result

def pow(N, A, x):
  result = default_matrix()

  while x:
    if x & 1:
      result = multiply(N, result, A)

    x >>= 1
    A = multiply(N, A, A)

  return result

def reduce(T, N, adj):
  result = [default_matrix()]

  for x in range(T):
    result.append(multiply(N, result[-1], adj[x]))

  return result

def solve(T, N, D, adj):
  # 1, 2, ..., T
  matrices = reduce(T, N, adj)

  if D == 0:
    return [[0] * N for _ in range(N)]

  return multiply(N, pow(N, matrices[T], D // T), matrices[D % T])

if __name__ == '__main__':
  T, N, D = map(int, input().split())
  adj = [[[0] * N for _ in range(N)] for _ in range(T)]

  for x in range(T):
    M = int(input())

    for _ in range(M):
      P, Q, C = map(int, input().split())
      adj[x][P - 1][Q - 1] = C

  for row in solve(T, N, D, adj):
    print(*row)
