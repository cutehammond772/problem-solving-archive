import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 100000

if __name__ == '__main__':
  N = int(input())
  result = INF

  for x in range(0, N + 1, 2):
    if not (N - x) % 5:
      result = min((N - x) // 5 + x // 2, result)

  print(result if result != INF else -1)
