import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(points):
  squares = set()

  for p in range(4):
    for q in range(p + 1, 4):
      x1, y1 = points[p]
      x2, y2 = points[q]

      squares.add((x1 - x2) ** 2 + (y1 - y2) ** 2)

  if len(squares) != 2:
    return 0

  if max(squares) == min(squares) * 2:
    return 1

  return 0

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    points = []

    for _ in range(4):
      x, y = map(int, input().split())
      points.append((x, y))

    print(solve(points))
  