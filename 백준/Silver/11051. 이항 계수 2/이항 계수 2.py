import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10007

if __name__ == '__main__':
  N, K = map(int, input().split())
  memo = [[0] * (N + 1) for _ in range(N + 1)]

  for p in range(1, N + 1):
    memo[p][0] = memo[p][p] = 1
    
    for q in range(1, p):
      memo[p][q] = (memo[p - 1][q] + memo[p - 1][q - 1]) % MOD

  print(memo[N][K])
