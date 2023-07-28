import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 2 * (10 ** 6) + 1

def solve(N, W, A):
  memo = [[INF] * (W + 1) for _ in range(W + 1)]
  trace = [[None] * (W + 1) for _ in range(W + 1)]

  def distance(first, second):
    a = A[first - 1] if first else (0, 0)
    b = A[second - 1] if second else (N - 1, N - 1)

    return abs(a[0] - b[0]) + abs(a[1] - b[1])

  # 0 -> 1
  memo[1][0], memo[0][1] = distance(0, 1), distance(1, 0)
  trace[1][0], trace[0][1] = (0, 0, 1), (0, 0, 2)

  for x in range(1, W):
    next = x + 1

    for t in range(2 * x):
      # 이전 바이토닉 수열
      if t >= x:
        a, b = (2 * x - 1) - t, x
      else:
        a, b = x, t

      # Case 1. 첫번째 경찰차를 이동
      if memo[next][b] > memo[a][b] + distance(a, next):
        memo[next][b] = memo[a][b] + distance(a, next)
        trace[next][b] = (a, b, 1)

      # Case 2. 두번째 경찰차를 이동
      if memo[a][next] > memo[a][b] + distance(next, b):
        memo[a][next] = memo[a][b] + distance(next, b)
        trace[a][next] = (a, b, 2)

  # 최소 거리 구하기 & 경로 역추적
  a, b, result = [INF] * 3
  nums = []

  for x in range(W + 1):
    for y in range(W + 1):
      if not (x == W or y == W):
        continue

      if result > memo[x][y]:
        a, b, result = x, y, memo[x][y]

  while trace[a][b]:
    nums.append(trace[a][b][2])
    a, b = trace[a][b][:2]

  return result, reversed(nums)

if __name__ == '__main__':
  N, W = int(input()), int(input())
  A = []

  for _ in range(W):
    X, Y = map(int, input().split())
    A.append((X - 1, Y - 1))

  total, nums = solve(N, W, A)

  print(total)
  print(*nums, sep='\n')
