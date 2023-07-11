import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  A, K = map(int, input().split())

  memo = [1000001] * (K + 1)
  memo[A] = 0

  for x in range(A, K):
    if x * 2 <= K:
      memo[x * 2] = min(memo[x * 2], memo[x] + 1)

    if x + 1 <= K:
      memo[x + 1] = min(memo[x + 1], memo[x] + 1)

  print(memo[K])
