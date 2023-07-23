import sys, math
input = lambda: sys.stdin.readline().rstrip()

NO_INTERSECTION = -1
INTERSECTS = 0
INTERSECTS_AT_VERTEX = 1
CONTAINS = 2

# 벡터의 외적을 통해 방향을 판별한다.
def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

  return 1 if result > 0 else -1 if result < 0 else 0

def compare(x1, y1, x2, y2):
  if x1 == x2:
    return y2 - y1

  return x2 - x1

def intersects(P, Q, V):
  x1, y1, x2, y2 = P
  x3, y3, x4, y4 = Q

  Px, Py = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
  Qx, Qy = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)

  Pxy, Qxy = Px * Py, Qx * Qy

  # 세 점 이상이 한 직선에 있는 경우 (1)
  if Pxy == Qxy == 0:
    if compare(x1, y1, x2, y2) < 0:
      x1, x2 = x2, x1
      y1, y2 = y2, y1

    if compare(x3, y3, x4, y4) < 0:
      x3, x4 = x4, x3
      y3, y4 = y4, y3

    # 끝점에서 만나는 경우 / 일부랑 겹치는 경우
    if compare(x1, y1, x4, y4) >= 0 and compare(x3, y3, x2, y2) >= 0:
      # Case 1: 세 점이 한 직선상에 존재
      if not (Px == Py == Qx == Qy == 0):
        if (x1, y1) == (x4, y4) or (x1, y1) == (x3, y3):
          V.add((x1, y1))

        elif (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4):
          V.add((x2, y2))

      # Case 2: 네 점이 한 직선상에 존재
      elif compare(x2, y2, x3, y3) == 0:
        V.add((x2, y2))

      elif compare(x1, y1, x4, y4) == 0:
        V.add((x1, y1))

      # Case 3: 일부 또는 전체가 겹치는 경우
      else:
        return CONTAINS

      return INTERSECTS_AT_VERTEX

    # 만나지 않는 경우
    else:
      return NO_INTERSECTION

  # 세 점 이상이 한 직선에 있는 경우 (2)
  elif Pxy < 0 and Qxy == 0:
    if Qx == 0:
      V.add((x1, y1))

    elif Qy == 0:
      V.add((x2, y2))

    return INTERSECTS_AT_VERTEX

  elif Pxy == 0 and Qxy < 0:
    if Px == 0:
      V.add((x3, y3))

    elif Py == 0:
      V.add((x4, y4))

    return INTERSECTS_AT_VERTEX

  # 선분의 중간에서 교차하는 경우
  elif Pxy < 0 and Qxy < 0:
    return INTERSECTS

  # 만나지 않는 경우
  else:
    return NO_INTERSECTION

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    xmin, ymin, xmax, ymax = map(int, input().split())
    L0 = tuple(map(int, input().split()))

    # 직사각형의 꼭짓점에서 만나는 경우
    V = set()

    # 직사각형의 선분의 중간에서 교차하는 경우
    intersection = 0

    # 직사각형의 선분
    L1 = (xmin, ymin, xmin, ymax)
    L2 = (xmin, ymin, xmax, ymin)
    L3 = (xmin, ymax, xmax, ymax)
    L4 = (xmax, ymin, xmax, ymax)

    for L in [L1, L2, L3, L4]:
      result = intersects(L, L0, V)

      if result == INTERSECTS:
        intersection += 1

      if result == CONTAINS:
        intersection = -1
        break

    if intersection == -1:
      print(4)
    else:
      print(intersection + len(V))
