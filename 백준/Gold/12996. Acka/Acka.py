import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

def combinations(N):
  memo = [[0] * (N + 1) for _ in range(N + 1)]

  # nCr = n-1Cr + n-1Cr-1
  for n in range(1, N + 1):
    for r in range(n + 1):
      if n == 1 or r == 0:
        memo[n][r] = 1
        continue

      memo[n][r] = (memo[n - 1][r] + memo[n - 1][r - 1]) % MOD

  return memo

def solve(S, a1, a2, a3):
  # 최대한 배정해도 S개의 곡에 모두 배정이 불가능한 경우이다.
  if a1 + a2 + a3 < S:
    return 0

  comb = combinations(S)

  # 전체 케이스
  result = [0] * (S + 1)
  min_bound = max(a1, a2, a3)

  for bound in range(min_bound, S + 1):
    # 참여하지 않은 곡 포함
    result[bound] = (comb[bound][a1] * comb[bound][a2] * comb[bound][a3]) % MOD

    # 참여하지 않은 곡의 개수에 따라 제외
    for k in range(1, (bound - min_bound) + 1):
      result[bound] = (result[bound] - (comb[bound][k] * result[bound - k])) % MOD

  return result[S]

if __name__ == "__main__":
  S, a1, a2, a3 = map(int, input().split())
  print(solve(S, a1, a2, a3))
