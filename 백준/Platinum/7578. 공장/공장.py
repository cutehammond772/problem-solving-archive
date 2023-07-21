import sys
input = lambda: sys.stdin.readline().rstrip()

def query(tree, q):
  result = 0

  while q:
    result += tree[q]
    q -= q & -q

  return result

def update(tree, q, x):
  while 0 < q < len(tree):
    tree[q] += x
    q += q & -q

def solve(N, A, B):
  result = 0

  # 구간합 펜윅 트리
  tree = [0] * (N + 1)

  # 인덱싱
  index = [0] * 1000001
  
  for xb in range(N):
    index[B[xb]] = xb

  for xa in range(N):
    xb = index[A[xa]]
    result += query(tree, N) - query(tree, xb + 1)

    update(tree, xb + 1, 1)

  return result

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]
  B = [*map(int, input().split())]

  print(solve(N, A, B))
