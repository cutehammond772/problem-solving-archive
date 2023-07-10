import sys, math, functools
input = lambda: sys.stdin.readline().rstrip()

def round(x):
  if x - int(x) >= 0.5:
    return int(x) + 1

  return int(x)

def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

  if result > 0:
    return 1
  elif result < 0:
    return -1

  return 0

def compare(x1, y1, x2, y2):
  result = x1 * y2 - x2 * y1

  if result != 0:
    return -result

  # 외적이 0인 경우, 세 점이 한 직선에 존재한다.
  if x1 != x2:
    return x1 - x2

  return y1 - y2

# Graham Scan
def convex_hull(N, dots):
  # 기준점 (x좌표, y좌표가 가장 작은 점 = 껍질에 무조건 포함되는 점)
  dots.sort()
  offset = dots[0]

  # 기울기에 따라 정렬한다. (반시계 방향..)
  dots = [offset] + sorted(
    dots[1:],
    key=functools.cmp_to_key(
      lambda p, q: compare(p[0] - offset[0], p[1] - offset[1], q[0] - offset[0], q[1] - offset[1])
    )
  )

  stack = [0, 1]
  next = 2

  while next < N:
    while len(stack) >= 2:
      second, first = stack.pop(), stack[-1]

      x1, y1 = dots[first]
      x2, y2 = dots[second]
      x3, y3 = dots[next]

      if ccw(x1, y1, x2, y2, x3, y3) > 0:
        stack.append(second)
        break

    stack.append(next)
    next += 1

  # 볼록 껍질의 둘레 계산
  result = 0.

  for t in range(len(stack) - 1, -1, -1):
    x1, y1 = dots[stack[t - 1]]
    x2, y2 = dots[stack[t]]

    result += ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

  return result

if __name__ == '__main__':
  N, L = map(int, input().split())
  dots = []

  for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))

  around = convex_hull(N, dots)
  circum = math.pi * L * 2

  print(round(around + circum))
