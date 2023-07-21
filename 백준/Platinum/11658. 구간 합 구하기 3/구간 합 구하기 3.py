import sys
input = lambda: sys.stdin.readline().rstrip()

def update(tree, row, col, x):
  p, q = row, col

  while 0 < p < len(tree):
    while 0 < q < len(tree):
      tree[p][q] += x
      q += q & -q

    p += p & -p
    q = col

def query(tree, row, col):
  result = 0
  p, q = row, col

  while p:
    while q:
      result += tree[p][q]
      q -= q & -q

    p -= p & -p
    q = col

  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  # 2차원 펜윅 트리
  tree = [[0] * (N + 1) for _ in range(N + 1)]

  for row in range(1, N + 1):
    for col in range(1, N + 1):
      update(tree, row, col, matrix[row - 1][col - 1])

  for _ in range(M):
    C, *K = map(int, input().split())

    if C == 0:
      row, col, val = K
      diff = val - matrix[row - 1][col - 1]

      update(tree, row, col, diff)
      matrix[row - 1][col - 1] += diff

    if C == 1:
      r1, c1, r2, c2 = K
      result = query(tree, r2, c2) - query(tree, r1 - 1, c2) - query(tree, r2, c1 - 1) + query(tree, r1 - 1, c1 - 1)

      print(result)
