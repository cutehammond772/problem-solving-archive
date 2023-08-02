import sys, math
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 9 + 1

def init(N, A):
  L = 2 ** (math.ceil(math.log2(N)) + 1)

  # [min, max, max-increase]
  tree = [[INF, -INF, -INF] for _ in range(L)]

  def make(node, left, right):
    if left == right:
      val = A[left]
      tree[node] = [val, val, 0]
      return

    mid = (left + right) // 2
    make(node * 2, left, mid)
    make(node * 2 + 1, mid + 1, right)

    tree[node] = [
      min(tree[node * 2][0], tree[node * 2 + 1][0]),
      max(tree[node * 2][1], tree[node * 2 + 1][1]),
      max(tree[node * 2][2], tree[node * 2 + 1][2], tree[node * 2 + 1][1] - tree[node * 2][0])
    ]

  make(1, 0, N - 1)
  return tree

def update(N, tree, x, k):
  def subroutine(node, left, right):
    if not (left <= x <= right):
      return

    if left == right:
      tree[node] = [k, k, 0]
      return

    mid = (left + right) // 2
    subroutine(node * 2, left, mid)
    subroutine(node * 2 + 1, mid + 1, right)

    tree[node] = [
      min(tree[node * 2][0], tree[node * 2 + 1][0]),
      max(tree[node * 2][1], tree[node * 2 + 1][1]),
      max(tree[node * 2][2], tree[node * 2 + 1][2], tree[node * 2 + 1][1] - tree[node * 2][0])
    ]

  subroutine(1, 0, N - 1)

def query(N, tree, x, y):
  def subroutine(node, left, right):
    if y < left or right < x:
      return [INF, -INF, -INF]

    if x <= left and right <= y:
      return tree[node]

    mid = (left + right) // 2
    A1 = subroutine(node * 2, left, mid)
    A2 = subroutine(node * 2 + 1, mid + 1, right)

    return [
      min(A1[0], A2[0]),
      max(A1[1], A2[1]),
      max(A1[2], A2[2], A2[1] - A1[0])
    ]

  return subroutine(1, 0, N - 1)

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]
  Q = int(input())

  tree = init(N, A)

  for _ in range(Q):
    C, X, Y = map(int, input().split())

    if C == 1:
      update(N, tree, X - 1, Y)

    elif C == 2:
      print(query(N, tree, X - 1, Y - 1)[2])
