import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 1_000_000_007

def inverse(k):
  # k ^ (MOD - 2) % MOD
  memo = [0] * 32
  result = 1
  
  for i in range(32):
    if i == 0:
      memo[i] = k % MOD
    else:
      memo[i] = (memo[i - 1] * memo[i - 1]) % MOD
      
    if (MOD - 2) & (1 << i) > 0:
      result = (result * memo[i]) % MOD
      
  return result
  

def modular(N, S):
  return (S * inverse(N)) % MOD

def solve(mods):
  result = 0
  
  for mod in mods:
    result = (result + mod) % MOD
    
  return result

if __name__ == '__main__':
  M = int(input())
  mods = [modular(*map(int, input().split())) for _ in range(M)]

  print(solve(mods))