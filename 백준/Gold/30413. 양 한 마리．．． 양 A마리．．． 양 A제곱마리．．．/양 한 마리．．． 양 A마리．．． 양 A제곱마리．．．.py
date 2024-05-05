import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

# 1, a, a2, a3, ... -> (a^n - 1) / (a - 1)
if __name__ == "__main__":
  A, B = map(int, input().split())
  
  if A == 1:
    print((A * B) % MOD)
  else:
    print(((pow(A, B, MOD) - 1) % MOD) * pow(A - 1, MOD - 2, MOD) % MOD)
  