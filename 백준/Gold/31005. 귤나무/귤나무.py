import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, A):
  total = sum(A)

  while total:
    M %= total

    total = 0

    for x in range(N):
      if total + A[x] > M:
        continue

      total += A[x]

  return M

if __name__ == '__main__':
  N, M = map(int, input().split())
  A = [*map(int, input().split())]

  print(solve(N, M, A))
