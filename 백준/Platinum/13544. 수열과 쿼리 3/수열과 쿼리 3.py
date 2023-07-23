import sys, math
input = lambda: sys.stdin.readline().rstrip()

# 머지 소트 트리 생성
def init(N, A):
  tree = [[] for _ in range(2 ** (math.ceil(math.log2(N)) + 1))]

  def merge(A, A1, A2):
    off_a1 = off_a2 = 0

    for _ in range(len(A1) + len(A2)):
      if off_a1 == len(A1):
        A.append(A2[off_a2])
        off_a2 += 1
      elif off_a2 == len(A2):
        A.append(A1[off_a1])
        off_a1 += 1
      else:
        if A1[off_a1] <= A2[off_a2]:
          A.append(A1[off_a1])
          off_a1 += 1
        else:
          A.append(A2[off_a2])
          off_a2 += 1

  def make(node, left, right):
    if left == right:
      tree[node].append(A[left])
      return

    mid = (left + right) // 2
    make(node * 2, left, mid)
    make(node * 2 + 1, mid + 1, right)

    # 합치기
    merge(tree[node], tree[node * 2], tree[node * 2 + 1])

  make(1, 0, N - 1)
  return tree

def upper_bound(A, K):
  x, y = 0, len(A)

  while x < y:
    mid = (x + y) // 2

    if A[mid] > K:
      y = mid
    else:
      x = mid + 1

  return x - 1

def query(N, tree, i, j, k):
  result = 0

  def recursion(node, left, right):
    nonlocal result

    if j < left or right < i:
      return

    if i <= left and right <= j:
      idx = upper_bound(tree[node], k)
      result += len(tree[node]) - (idx + 1)
      return

    mid = (left + right) // 2
    recursion(node * 2, left, mid)
    recursion(node * 2 + 1, mid + 1, right)

  recursion(1, 0, N - 1)
  return result

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  tree = init(N, A)
  last = 0

  M = int(input())
  for _ in range(M):
    a, b, c = map(int, input().split())

    # XOR 처리
    i, j, k = a ^ last, b ^ last, c ^ last
    print(last := query(N, tree, i - 1, j - 1, k))
