import sys
input = lambda: sys.stdin.readline().rstrip()

# 소수이다.
MOD = 1000000007

def factorials(N):
  result = [1]
  
  for X in range(1, N + 1):
    result.append((result[-1] * X) % MOD)
  
  return result

def pow(X, Y):
  result = 1
  X = X % MOD
  
  while Y:
    if Y & 1:
      result = (result * X) % MOD
    
    Y >>= 1
    X = (X * X) % MOD
  
  return result

def solver():
  # (0! ~ 4000000!) % MOD까지 구한다.
  F = factorials(4000000)
  
  # N! * (R!(N - R)!) ^ (MOD - 2) % MOD
  def solve(N, R):
    return F[N] * pow((F[R] * F[N - R]) % MOD, MOD - 2) % MOD
  
  return solve

if __name__ == '__main__':
  N = int(input())
  solve = solver()
  
  for _ in range(N):
    N, R = map(int, input().split())
    print(solve(N, R))
    