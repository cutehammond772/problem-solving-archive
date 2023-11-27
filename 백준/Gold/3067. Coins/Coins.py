import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, C):
  memo = [0] * (M + 1)
  memo[0] = 1

  for x in range(N):
    coin = C[x]

    for amount in range(coin, M + 1):
      memo[amount] += memo[amount - coin]

  return memo[M]

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N = int(input())
    C = [*map(int, input().split())]
    M = int(input())

    print(solve(N, M, C))
