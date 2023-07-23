import sys, math
from functools import cmp_to_key
input = lambda: sys.stdin.readline().rstrip()
INF = 10001.0

# 벡터의 외적을 통해 방향을 판별한다.
def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

  return 1 if result > 0 else -1 if result < 0 else 0

# 두 위치 벡터의 외적을 통해 비교한다.
def comparator(offset):
  def compare(d1, d2):
    x1, y1 = d1[0] - offset[0], d1[1] - offset[1]
    x2, y2 = d2[0] - offset[0], d2[1] - offset[1]

    result = x1 * y2 - x2 * y1

    if result != 0:
      return -result

    # 세 점이 한 직선에 존재하는 경우 (외적이 0일 떄)
    if x1 != x2:
      return x1 - x2

    return y1 - y2

  return compare

def solve(N, dots):
  # 1. 기준점을 하나 정한다.
  # (x, y)가 가장 작은 점 = 가장 바깥 점 = 껍질에 무조건 포함되는 점
  dots.sort()
  offset = dots[0]

  # 2. 외적을 이용하여 정렬한다.
  compare = comparator(offset)
  dots = dots[1:]

  dots.sort(key=cmp_to_key(compare))
  dots = [offset] + dots

  # 3. Graham Scan을 이용하여 볼록 껍질을 찾는다.
  hull = [0, 1]
  next = 2

  while next < N:
    while len(hull) >= 2:
      second, first = hull.pop(), hull[-1]

      x1, y1 = dots[first]
      x2, y2 = dots[second]
      x3, y3 = dots[next]

      if ccw(x1, y1, x2, y2, x3, y3) > 0:
        hull.append(second)
        break

    hull.append(next)
    next += 1

  # 4. 직선과 점 사이의 거리의 최소를 찾는다.
  result = INF
  H = len(hull)

  # 가능한 선분들이다.
  lines = [(x - 1, x) for x in range(1, H)] + [(0, H - 1)]

  for d1, d2 in lines:
    x1, y1 = dots[hull[d1]]
    x2, y2 = dots[hull[d2]]
    denominator = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    dist = 0.

    for another in range(H):
      if another == d1 or another == d2:
        continue

      x0, y0 = dots[hull[another]]
      numerator = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
      dist = max(dist, numerator / denominator)

    result = min(result, dist)

  # 소수점 0.01배수 올림
  return math.ceil(result * 100.) / 100.

if __name__ == '__main__':
  case = 0

  while N := int(input()):
    dots = []

    for _ in range(N):
      X, Y = map(int, input().split())
      dots.append((X, Y))

    result = solve(N, dots)
    print(f"Case {(case := case + 1)}: {result:.2f}")
