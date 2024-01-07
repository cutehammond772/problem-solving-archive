import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
  # memo[a][b] -> [a, b] 구간에서 선공, 후공의 점수
  memo = [[(0, 0)] * N for _ in range(N)]

  # 구간의 크기를 1씩 늘릴 때마다 선공, 후공의 위치가 바뀌는 점에 유의한다.
  for s in range(N):
    for a in range(N - s):
      if s == 0:
        memo[a][a + s] = (A[a], 0)
        continue

      lf, ls = memo[a + 1][a + s]
      rf, rs = memo[a][a + s - 1]

      memo[a][a + s] = max((ls + A[a], lf), (rs + A[a + s], rf))

  return memo[0][N - 1][0]

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N = int(input())
    A = [*map(int, input().split())]

    print(solve(N, A))
