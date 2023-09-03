import sys
input = lambda: sys.stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
  return 1 if result > 0 else -1 if result < 0 else 0

if __name__ == '__main__':
  x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
  P1, P2 = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
  Q1, Q2 = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)

  if P1 * P2 < 0 and Q1 * Q2 < 0:
    print(1)
  else:
    print(0)
