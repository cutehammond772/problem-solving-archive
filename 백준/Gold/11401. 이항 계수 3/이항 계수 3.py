import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

def factorials(N):
  result = [1]

  for t in range(1, N + 1):
    result.append((result[-1] * t) % MOD)

  return result

def pow(x, p):
  result = 1

  while p:
    if p & 1:
      result = (result * x) % MOD

    p >>= 1
    x = (x ** 2) % MOD

  return result

# NCK % MOD = (N! / (K!(N-K)!)) % MOD
# = ((N! % MOD) * ((K!) ^ (MOD - 2) % MOD) * (((N - K)!) ^ (MOD - 2) % MOD)) % MOD
def solve(N, K):
  F = factorials(N)
  
  return F[N] * pow(F[K], MOD - 2) * pow(F[N - K], MOD - 2) % MOD

if __name__ == "__main__":
  N, K = map(int, input().split())
  print(solve(N, K))
