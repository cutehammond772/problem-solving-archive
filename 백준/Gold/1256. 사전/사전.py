import sys
input = lambda: sys.stdin.readline().rstrip()

memo = [[0] * 201 for _ in range(201)]

for n in range(1, 201):
  for r in range(n + 1):
    if n == 1 or r == 0:
      memo[n][r] = 1
      continue

    memo[n][r] = memo[n - 1][r] + memo[n - 1][r - 1]

def solve(N, M, K):
  result = ""

  while K > 0 and N + M > 0:
    if N == 0 or M == 0:
      break

    comb = memo[(N + M) - 1][N - 1]
    
    if K > comb:
      K -= comb
      result += "z"
      M -= 1

    else:
      result += "a"
      N -= 1
  
  if K > 1:
    return -1

  result += ("a" * N) + ("z" * M)
  return result

if __name__ == '__main__':
  N, M, K = map(int, input().split())
  print(solve(N, M, K))
