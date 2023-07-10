import sys
input = lambda: sys.stdin.readline().rstrip()
MAX_LEN = 50

def mod(S, K):
  result = 0
  
  for ch in S:
    result = (result * 10 + int(ch)) % K
    
  return result, len(S)

def powers(N, K):
  result = [1 % K]
  for x in range(1, N + 1):
    result.append((result[-1] * 10) % K)
  
  return result

def gcd(P, Q):
  while Q:
    P, Q = Q, P % Q
  
  return P

# N * (10^K) % MOD = (N % MOD) * ((10^K) % MOD) % MOD
def solve(N, K, Q):
  Q = [mod(S, K) for S in Q]
  T = powers(MAX_LEN, K)
  
  memo = [[0] * K for _ in range(2 ** N)]
  numbers = [set() for _ in range(N + 1)]
  
  # 초기값 설정
  for x in range(N):
    p, q = Q[x]
    
    memo[1 << x][p] += 1
    numbers[1].add(1 << x)
  
  for idx in range(2, N + 1):
    for num in numbers[idx - 1]:
      for n in range(N):
        if num & (1 << n):
          continue
        
        p, q = Q[n]
        next = num | (1 << n)
        numbers[idx].add(next)
        
        for k in range(K):
          if memo[num][k] == 0:
            continue
            
          m = (k * T[q] + p) % K
          memo[next][m] += memo[num][k]
          
  return memo[(2 ** N) - 1][0]

if __name__ == '__main__':
  N = int(input())
  sequences = [input() for _ in range(N)]
  K = int(input())
  
  numerator = solve(N, K, sequences)
  denominator = 1
  
  for x in range(2, N + 1):
    if numerator % x == 0:
      numerator //= x
      continue
    
    denominator *= x
  
  G = gcd(denominator, numerator)
  numerator //= G
  denominator //= G
  
  print(f"{numerator}/{denominator}")
  