import sys
input = lambda: sys.stdin.readline().rstrip()
T = 10 ** 6

def update(tree, q, x):
  while 0 < q < len(tree):
    tree[q] += x
    q += q & -q

def query(tree, q):
  result = 0

  while q:
    result += tree[q]
    q -= q & -q

  return result

if __name__ == '__main__':
  N = int(input())

  # 펜윅 트리 (1 ~ 10^6)
  tree = [0] * (T + 1)

  for _ in range(N):
    A, *BC = map(int, input().split())

    if A == 1:
      priority = BC[0]
      x, y = 1, T

      while x < y:
        mid = (x + y) // 2
        K = query(tree, mid)

        if K >= priority:
          y = mid
        else:
          x = mid + 1

      print(x)
      update(tree, x, -1)

    if A == 2:
      update(tree, BC[0], BC[1])
      