import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N = int(input())
    comb = [[0] * N for _ in range(N)]
    total = 0

    for p in range(N - 1):
      data = [*map(int, input().split())]
      size = (N - 1) - p

      for q in range(size):
        comb[p][p + q + 1] = comb[p + q + 1][p] = data[q]

    for p in range(N):
      colors = [0, 0]

      for q in range(N):
        if p == q:
          continue

        colors[comb[p][q]] += 1

      total += colors[0] * colors[1]

    print((N * (N - 1) * (N - 2) // 6) - (total // 2))
