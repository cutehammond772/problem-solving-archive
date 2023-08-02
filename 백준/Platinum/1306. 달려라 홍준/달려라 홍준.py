import sys, math
input = lambda: sys.stdin.readline().rstrip()

def init(N, A):
  tree = [0] * (2 ** (math.ceil(math.log2(N)) + 1))

  def make(node, left, right):
    if left == right:
      tree[node] = A[left]
      return

    mid = (left + right) // 2
    make(node * 2, left, mid)
    make(node * 2 + 1, mid + 1, right)

    tree[node] = max(tree[node * 2], tree[node * 2 + 1])

  make(1, 0, N - 1)
  return tree

def query(N, tree, x, y):
  def subquery(node, left, right):
    if x <= left and right <= y:
      return tree[node]

    if y < left or right < x:
      return 0

    mid = (left + right) // 2
    return max(subquery(node * 2, left, mid), subquery(node * 2 + 1, mid + 1, right))

  return subquery(1, 0, N - 1)

def solve(N, M, A):
  result = []
  tree = init(N, A)

  for x in range(M - 1, N - (M - 1)):
    result.append(query(N, tree, x - (M - 1), x + (M - 1)))

  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  A = [*map(int, input().split())]

  print(*solve(N, M, A))
