import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
  x, y = 0, len(A)

  while x < y:
    mid = (x + y) // 2

    if A[mid] >= K:
      y = mid
    else:
      x = mid + 1

  return x


def upper_bound(A, K):
  x, y = 0, len(A)

  while x < y:
    mid = (x + y) // 2

    if A[mid] > K:
      y = mid
    else:
      x = mid + 1

  return x

def solve(A, B):
  # 한 쪽만 정렬하면 된다.
  B.sort()
  win, draw, lose = 0, 0, 0

  for x in A:
    p, q = lower_bound(B, x), upper_bound(B, x)
    win += p
    draw += q - p
    lose += len(B) - q

  return win, lose, draw

if __name__ == '__main__':
  _, _ = map(int, input().split())
  A = [*map(int, input().split())]
  B = [*map(int, input().split())]

  print(*solve(A, B))
