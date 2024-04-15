import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9)

def solve(N):
  memo = [0] * max(3, N + 1)
  
  # 2의 경우 별도로 정해줘야 한다.
  memo[2] = 1
  
  for x in range(3, N + 1):
    memo[x] = ((x - 1) * (memo[x - 1] + memo[x - 2])) % MOD
  
  return memo[N]

if __name__ == "__main__":
  N = int(input())
  print(solve(N))
  