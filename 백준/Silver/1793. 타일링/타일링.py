import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  while data := input():
    N = int(data)

    if N < 2:
      print([1, 1][N])
      continue

    memo = [0] * (N + 1)
    memo[1], memo[2] = 1, 3

    for x in range(3, N + 1):
      memo[x] = memo[x - 1] + memo[x - 2] * 2

    print(memo[N])
