import sys, math
input = lambda: sys.stdin.readline().rstrip()

def init(N, A):
  L = 2 ** (math.ceil(math.log2(N)) + 1)
  tree, lazy = [0] * L, [0] * L

  def make(node, left, right):
    if left == right:
      tree[node] = A[left]
      return

    mid = (left + right) // 2
    make(node * 2, left, mid)
    make(node * 2 + 1, mid + 1, right)

    tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

  def propagate(node, left, right):
    if not lazy[node]:
      return

    if (right - left + 1) % 2:
      tree[node] ^= lazy[node]

    if left != right:
      lazy[node * 2] ^= lazy[node]
      lazy[node * 2 + 1] ^= lazy[node]

    lazy[node] = 0

  def query(x, y):
    def subquery(node, left, right):
      propagate(node, left, right)

      if x <= left and right <= y:
        return tree[node]

      if y < left or right < x:
        return 0

      mid = (left + right) // 2
      return subquery(node * 2, left, mid) ^ subquery(node * 2 + 1, mid + 1, right)

    return subquery(1, 0, N - 1)

  def update(x, y, k):
    def subroutine(node, left, right):
      propagate(node, left, right)

      if x <= left and right <= y:
        if (right - left + 1) % 2:
          tree[node] ^= k

        if left != right:
          lazy[node * 2] ^= k
          lazy[node * 2 + 1] ^= k

        return

      if y < left or right < x:
        return

      mid = (left + right) // 2
      subroutine(node * 2, left, mid)
      subroutine(node * 2 + 1, mid + 1, right)

      tree[node] = tree[node * 2] ^ tree[node * 2 + 1]

    subroutine(1, 0, N - 1)

  make(1, 0, N - 1)
  return update, query

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  update, query = init(N, A)
  M = int(input())

  for _ in range(M):
    C, *K = map(int, input().split())

    if C == 1:
      update(*K)

    elif C == 2:
      print(query(*K))
