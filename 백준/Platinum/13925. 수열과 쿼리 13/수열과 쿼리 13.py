import sys, math
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7
ADD, MUL, SET = 1, 2, 3

def init(N, A):
  L = 2 ** (math.ceil(math.log2(N)) + 1)
  # ax + b 형태로 lazy 배열을 관리
  tree, lazy = [0] * L, [[1, 0] for _ in range(L)]

  def make(node, left, right):
    if left == right:
      tree[node] = A[left] % MOD
      return

    mid = (left + right) // 2
    make(node * 2, left, mid)
    make(node * 2 + 1, mid + 1, right)

    tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

  def propagate(node, left, right):
    a, b = lazy[node]
    tree[node] = (a * tree[node] + b * (right - left + 1)) % MOD

    if left != right:
      a1, b1 = lazy[node * 2]
      a2, b2 = lazy[node * 2 + 1]

      lazy[node * 2] = [(a * a1) % MOD, (a * b1 + b) % MOD]
      lazy[node * 2 + 1] = [(a * a2) % MOD, (a * b2 + b) % MOD]

    lazy[node] = [1, 0]

  def query(x, y, node, left, right):
    propagate(node, left, right)

    if x <= left and right <= y:
      return tree[node]

    if y < left or right < x:
      return 0

    mid = (left + right) // 2
    return (query(x, y, node * 2, left, mid) + query(x, y, node * 2 + 1, mid + 1, right)) % MOD

  def update(x, y, v, cmd, node, left, right):
    propagate(node, left, right)

    if x <= left and right <= y:
      if cmd == ADD:
        tree[node] = (tree[node] + (v * (right - left + 1))) % MOD

        if left != right:
          a1, b1 = lazy[node * 2]
          a2, b2 = lazy[node * 2 + 1]

          lazy[node * 2] = [a1, (b1 + v) % MOD]
          lazy[node * 2 + 1] = [a2, (b2 + v) % MOD]

      elif cmd == MUL:
        tree[node] = (tree[node] * v) % MOD

        if left != right:
          a1, b1 = lazy[node * 2]
          a2, b2 = lazy[node * 2 + 1]

          lazy[node * 2] = [(a1 * v) % MOD, (b1 * v) % MOD]
          lazy[node * 2 + 1] = [(a2 * v) % MOD, (b2 * v) % MOD]

      elif cmd == SET:
        tree[node] = (v * (right - left + 1)) % MOD

        if left != right:
          lazy[node * 2] = [0, v]
          lazy[node * 2 + 1] = [0, v]

      return

    if y < left or right < x:
      return

    mid = (left + right) // 2
    update(x, y, v, cmd, node * 2, left, mid)
    update(x, y, v, cmd, node * 2 + 1, mid + 1, right)

    tree[node] = (tree[node * 2] + tree[node * 2 + 1]) % MOD

  make(1, 0, N - 1)
  return update, query

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  update, query = init(N, A)
  M = int(input())

  for _ in range(M):
    C, *K = map(int, input().split())

    # ADD, MUL, SET
    if 1 <= C <= 3:
      x, y, v = K
      update(x - 1, y - 1, v, C, 1, 0, N - 1)

    # SUM
    elif C == 4:
      x, y = K
      print(query(x - 1, y - 1, 1, 0, N - 1))
