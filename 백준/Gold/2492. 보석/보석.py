import sys
input = lambda: sys.stdin.readline().rstrip()

def axis(S):
  xs, ys = [], []

  for x, y in S:
    xs.append(x)
    ys.append(y)

  xs, ys = [*sorted(set(xs))], [*sorted(set(ys))]

  return xs, ys

def count(x1, x2, y1, y2, S):
  result = 0

  for x, y in S:
    result += (x1 <= x <= x2) and (y1 <= y <= y2)

  return result

def left(p, q):
  if p < 0:
    p, q = 0, q - p

  return p, q

def right(p, q, bound):
  if q > bound:
    p, q = p - (q - bound), bound

  return p, q

def solve(N, M, K, S):
  # 금광석이 존재하는 x축, y축으로 나눈다.
  xs, ys = axis(S)

  # (total, x, y)
  result = (0, 0, 0)

  for x in xs:
    xl, xr = left(x - K, x), right(x, x + K, N)

    for y in ys:
      yl, yr = left(y - K, y), right(y, y + K, M)

      result = max(result,
                   (count(*xl, *yl, S), xl[0], yl[1]),
                   (count(*xl, *yr, S), xl[0], yr[1]),
                   (count(*xr, *yl, S), xr[0], yl[1]),
                   (count(*xr, *yr, S), xr[0], yr[1])
                  )

  return result

if __name__ == '__main__':
  N, M, T, K = map(int, input().split())

  # 금광석의 좌표
  S = []

  for _ in range(T):
    x, y = map(int, input().split())
    S.append((x, y))

  # 정사각형의 (left, top) 및 최대 개수
  total, x, y = solve(N, M, K, S)

  print(x, y)
  print(total)
