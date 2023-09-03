import sys
input = lambda: sys.stdin.readline().rstrip()
MAX = 301

if __name__ == '__main__':
  N, M, K = map(int, input().split())
  memo = [[-1] * MAX for _ in range(MAX)]

  # 처음에는 M, K개가 남아있다.
  memo[M][K] = 0

  for _ in range(N):
    x, y = map(int, input().split())

    for p in range(MAX):
      for q in range(MAX):
        if memo[p][q] < 0 or not (p >= x and q >= y):
          continue

        memo[p - x][q - y] = max(memo[p - x][q - y], memo[p][q] + 1)

  print(max(max(lst) for lst in memo))
