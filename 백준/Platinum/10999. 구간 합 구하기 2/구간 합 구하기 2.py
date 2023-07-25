import sys, math
input = lambda: sys.stdin.readline().rstrip()

def create(N, A):
  L = 2 ** (math.ceil(math.log2(N)) + 1)
  tree, lazy = [0] * L, [0] * L

  def subroutine(node, left, right):
    if left == right:
      tree[node] = A[left]
      return

    mid = (left + right) // 2
    subroutine(node * 2, left, mid)
    subroutine(node * 2 + 1, mid + 1, right)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

  subroutine(1, 0, N - 1)
  return tree, lazy

def propagate(tree, lazy, node, left, right):
  if lazy[node]:
    tree[node] += lazy[node] * (right - left + 1)

    if left != right:
      lazy[node * 2] += lazy[node]
      lazy[node * 2 + 1] += lazy[node]

    lazy[node] = 0

def update(N, tree, lazy, i, j, k):
  def subroutine(node, left, right):
    # 트리 갱신
    propagate(tree, lazy, node, left, right)

    if j < left or right < i:
      return

    if i <= left and right <= j:
      tree[node] += (right - left + 1) * k

      if left != right:
        lazy[node * 2] += k
        lazy[node * 2 + 1] += k

      return

    mid = (left + right) // 2
    subroutine(node * 2, left, mid)
    subroutine(node * 2 + 1, mid + 1, right)

    tree[node] = tree[node * 2] + tree[node * 2 + 1]

  subroutine(1, 0, N - 1)

def query(N, tree, lazy, x, y):
  def subroutine(node, left, right):
    # 트리 갱신
    propagate(tree, lazy, node, left, right)

    # 기존 세그먼트 트리
    if y < left or right < x:
      return 0

    if x <= left and right <= y:
      return tree[node]

    mid = (left + right) // 2
    return subroutine(node * 2, left, mid) + subroutine(node * 2 + 1, mid + 1, right)

  return subroutine(1, 0, N - 1)

if __name__ == '__main__':
  N, M, K = map(int, input().split())
  A = [int(input()) for _ in range(N)]
  tree, lazy = create(N, A)

  for _ in range(M + K):
    C, *args = map(int, input().split())

    if C == 1:
      i, j, k = args
      update(N, tree, lazy, i - 1, j - 1, k)

    elif C == 2:
      i, j = args
      print(query(N, tree, lazy, i - 1, j - 1))
