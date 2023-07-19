import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 20000 ** 2 + 1

def dist(P, Q):
  return (P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2

# 분할 정복 이용
def solve(dots, P, Q):
  if P == Q:
    return INF

  if Q - P == 1:
    return dist(dots[P], dots[Q])

  mid = (P + Q) // 2

  # 1. 각 두 영역에 대해 계산
  result = min(solve(dots, P, mid), solve(dots, mid + 1, Q))

  # 2. 중간 영역에 대해 최단거리 계산
  candidates = []

  for k in range(P, Q + 1):
    if (dots[mid][0] - dots[k][0]) ** 2 >= result:
      continue

    candidates.append(k)

  # 2-1. y값 기준으로 정렬
  candidates.sort(key=lambda k: dots[k][1])

  # 2-2. 영역 내 두 점을 골라 최단거리 정하기
  for p in range(len(candidates)):
    for q in range(p + 1, len(candidates)):
      if (dots[candidates[p]][1] - dots[candidates[q]][1]) ** 2 >= result:
        break

      result = min(result, dist(dots[candidates[p]], dots[candidates[q]]))

  return result

if __name__ == '__main__':
  N = int(input())
  dots = []

  for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

  dots.sort()
  print(solve(dots, 0, N - 1))
