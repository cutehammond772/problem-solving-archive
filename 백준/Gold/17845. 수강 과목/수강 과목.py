import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
  N, K = map(int, input().split())
  memo = [-1] * (N + 1)
  memo[0] = 0

  for _ in range(K):
    I, T = map(int, input().split())

    for time in range(N, T - 1, -1):
      memo[time] = max(memo[time], memo[time - T] + I)

  print(max(memo))
