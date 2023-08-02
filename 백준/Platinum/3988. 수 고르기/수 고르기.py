import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
INF = 20000001

# 1. Monotone Queue 테크닉을 이용한다. (= 최솟값)
# 2. 최대값은 무조건 [x, x + (N - K) - 1]의 양끝의 차이다.
if __name__ == '__main__':
  N, K = map(int, input().split())
  V = [*sorted(map(int, input().split()))]

  result = INF

  idx = 1
  queue = deque([])

  # 슬라이딩 윈도우
  for offset in range(K + 1):
    # 범위에 해당되지 않는 원소를 제거한다.
    if queue and queue[0] <= offset:
      queue.popleft()

    # 최솟값을 구성하는 (두) 원소를 모두 저장하는 것이 아니라, 최솟값의 대표가 되는 원소만 저장한다.
    for x in range(idx, offset + (N - K)):
      while queue and (V[x] - V[x - 1]) <= (V[queue[-1]] - V[queue[-1] - 1]):
        queue.pop()

      queue.append(x)

    idx = offset + (N - K)
    M, m = V[idx - 1] - V[offset], V[queue[0]] - V[queue[0] - 1]

    result = min(result, M + m)

  print(result)
