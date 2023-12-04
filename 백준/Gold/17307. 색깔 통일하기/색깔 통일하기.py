import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 18

# 특정 버튼 위치를 기준으로 양쪽 차(diff) 누적합을 비교한다.
def solve(N, C, X):
  left, right = [0] * N, [0] * N

  # (count, button)
  result = (INF, INF)

  def diff(x):
    return C + x if x < 0 else x

  # 1. 누적합 계산
  for i in range(1, N):
    left[i] = left[i - 1] + diff(X[i - 1] - X[i])
    right[(N - 1) - i] = right[N - i] + diff(X[N - i] - X[(N - 1) - i])

  # 2-1. 맨 우측 버튼
  result = min(result, (left[-1], N))

  # 2-2. 맨 좌측 버튼
  result = min(result, (right[0], 1))

  # 2-3. 중간 버튼
  for i in range(1, N - 1):
    result = min(result, (max(left[i], right[i]), i + 1))

  return result

if __name__ == '__main__':
  N, C = map(int, input().split())
  X = [*map(int, input().split())]

  count, button = solve(N, C, X)

  print(button)
  print(count)
