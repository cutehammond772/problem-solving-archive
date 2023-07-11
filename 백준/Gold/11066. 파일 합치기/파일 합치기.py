import sys
input = lambda: sys.stdin.readline().rstrip()

NaN = 2 ** 63 - 1

def solve(K, files):
  # (sum, cost)
  memo = [[(NaN, NaN)] * K for _ in range(K)]

  for y in range(K):
    for x in range(K - y):
      if y == 0:
        memo[x][x] = (files[x], 0)
        continue
        
      for k in range(y):
        left_sum, left_cost = memo[x][x + k]
        right_sum, right_cost = memo[x + k + 1][x + y]
        
        sum = left_sum + right_sum
        cost = left_cost + right_cost + sum

        if memo[x][x + y][1] > cost:
          memo[x][x + y] = (sum, cost)

  return memo[0][K - 1][1]

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    print(solve(K, files))