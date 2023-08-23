import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N, K = map(int, input().split())

  memo = [[0] * (K + 1) for _ in range(N)]
  donations = []

  for x in range(N):
    P1, P2, Q1, Q2 = map(int, input().split())
    donations.append((P1, P2, Q1, Q2))

    if x == 0:
      if P1 <= K:
        memo[0][P1] = P2

      if Q1 <= K:
        memo[0][Q1] = Q2

  for x in range(1, N):
    P1, P2, Q1, Q2 = donations[x]

    for y in range(1, K + 1):
      if not memo[x - 1][y]:
        continue

      if y + P1 <= K:
        memo[x][y + P1] = max(memo[x][y + P1], memo[x - 1][y] + P2)

      if y + Q1 <= K:
        memo[x][y + Q1] = max(memo[x][y + Q1], memo[x - 1][y] + Q2)

  print(max(memo[-1]))
