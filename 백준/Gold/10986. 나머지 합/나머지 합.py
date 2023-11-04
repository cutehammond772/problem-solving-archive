import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, A):
  memo = [0] * M
  accu, result = 0, 0

  for i in range(N):
    accu = (accu + A[i]) % M
    memo[accu] += 1

  m0 = memo[0]
  result += m0 * (m0 + 1) // 2

  for i in range(1, M):
    mi = memo[i] - 1

    if mi > 0:
      result += mi * (mi + 1) // 2

  return result

if __name__ == "__main__":
  N, M = map(int, input().split())
  A = [*map(int, input().split())]

  print(solve(N, M, A))
