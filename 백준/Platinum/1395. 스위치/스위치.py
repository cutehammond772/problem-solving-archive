import sys, math
input = lambda: sys.stdin.readline().rstrip()

def init(N):
  L = 2 ** (math.ceil(math.log2(N)) + 1)
  tree, lazy = [0] * L, [0] * L

  def propagate(node, left, right):
    if not lazy[node]:
      return

    if left != right:
      lazy[node * 2] += lazy[node]
      lazy[node * 2 + 1] += lazy[node]

    if lazy[node] % 2:
      tree[node] = (right - left + 1) - tree[node]

    lazy[node] = 0

  def update(x, y):
    def subroutine(node, left, right):
      propagate(node, left, right)

      if y < left or right < x:
        return

      if x <= left and right <= y:
        tree[node] = (right - left + 1) - tree[node]

        if left != right:
          lazy[node * 2] += 1
          lazy[node * 2 + 1] += 1

        return

      mid = (left + right) // 2
      subroutine(node * 2, left, mid)
      subroutine(node * 2 + 1, mid + 1, right)

      tree[node] = tree[node * 2] + tree[node * 2 + 1]

    subroutine(1, 0, N - 1)

  def query(x, y):
    def subroutine(node, left, right):
      propagate(node, left, right)

      if y < left or right < x:
        return 0

      if x <= left and right <= y:
        return tree[node]

      mid = (left + right) // 2
      return subroutine(node * 2, left, mid) + subroutine(node * 2 + 1, mid + 1, right)

    return subroutine(1, 0, N - 1)

  return update, query

if __name__ == '__main__':
  N, M = map(int, input().split())
  update, query = init(N)

  for _ in range(M):
    op, S, T = map(int, input().split())

    if op == 0:
      update(S - 1, T - 1)

    if op == 1:
      print(query(S - 1, T - 1))
