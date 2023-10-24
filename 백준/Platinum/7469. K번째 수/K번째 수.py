import sys
input = lambda: sys.stdin.readline().rstrip()
MIN, MAX = -(10 ** 9), 10 ** 9

def upper_bound(A, K):
  x, y = 0, len(A)

  while x < y:
    mid = (x + y) // 2

    if A[mid] > K:
      y = mid
    else:
      x = mid + 1

  return x

def init(tree, A, node, left, right):
  if left == right:
    tree[node].append(A[left])
    return

  mid = (left + right) // 2
  init(tree, A, node * 2, left, mid)
  init(tree, A, node * 2 + 1, mid + 1, right)

  # merge 과정
  lt, rt = tree[node * 2], tree[node * 2 + 1]
  lp, rp = 0, 0

  for _ in range(len(lt) + len(rt)):
    if lp >= len(lt):
      tree[node].append(rt[rp])
      rp += 1
      continue

    if rp >= len(rt):
      tree[node].append(lt[lp])
      lp += 1
      continue

    if lt[lp] <= rt[rp]:
      tree[node].append(lt[lp])
      lp += 1
    else:
      tree[node].append(rt[rp])
      rp += 1

def query(tree, x, i, j, node, left, right):
  if right < i or j < left:
    return 0

  if i <= left and right <= j:
    return upper_bound(tree[node], x)

  mid = (left + right) // 2
  lt, rt = query(tree, x, i, j, node * 2, left, mid), query(tree, x, i, j, node * 2 + 1, mid + 1, right)

  return lt + rt

def solve(N, A, queries):
  node = [1, 1, N]

  tree = [[] for _ in range(N * 4)]
  result = []

  # 머지 소트 트리를 초기화한다.
  init(tree, A, *node)

  # 각 쿼리를 처리한다.
  for i, j, k in queries:
    x, y = MIN, MAX

    while x < y:
      mid = (x + y) // 2
      order = query(tree, mid, i, j, *node)

      # Parametric Search
      if order >= k:
        y = mid
      else:
        x = mid + 1

    result.append(x)

  return result

if __name__ == "__main__":
  N, Q = map(int, input().split())
  A = [0, *map(int, input().split())]
  queries = []

  for _ in range(Q):
    i, j, k = map(int, input().split())
    queries.append((i, j, k))

  result = solve(N, A, queries)
  print(*result, sep='\n')
