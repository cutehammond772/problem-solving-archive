import sys
input = lambda: sys.stdin.readline().rstrip()

# 이어지는 판자끼리 구간을 합친다.
def combine(Q):
  result = []

  # 판자의 위치(L, R)을 기준으로 정렬
  Q.sort()

  # 이어진 판자의 계산
  min_left, max_right = 0, 0

  for L, R in Q:
    # 더이상 판자가 이어지지 않는 경우
    if max_right < L:
      result.append((min_left, max_right))
      min_left = max_right = L

    # 판자로 이어지는 경우
    min_left = min(min_left, L)
    max_right = max(max_right, R)

  result.append((min_left, max_right))

  return result

def solve(Q):
  Q = combine(Q)
  max_dist, max_reach = 0, 0

  for L, R in Q:
    # 이전 판자에서 도달이 불가능한 경우
    if max_dist < L:
      break

    max_reach = R
    max_dist = max(max_dist, R + (R - L))

  return max_reach

if __name__ == "__main__":
  N = int(input())
  Q = []

  for _ in range(N):
    L, R = map(int, input().split())
    Q.append((L, R))

  print(solve(Q))
