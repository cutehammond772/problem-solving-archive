import sys
input = lambda: sys.stdin.readline().rstrip()

# 좌표 압축
def compress(C):
  ordered = [*sorted(range(len(C)), key=lambda x: C[x])]
  order, previous = 0, -1

  for x in ordered:
    if C[x] != previous:
      order += 1

    previous = C[x]
    C[x] = order

def update(tree, q, x):
  while 0 < q < len(tree):
    tree[q] += x
    q += q & -q

def query(tree, q):
  result = 0

  while q:
    result += tree[q]
    q -= q & -q

  return result

if __name__ == '__main__':
  N = int(input())
  order = [int(input()) for _ in range(N)]
  compress(order)

  # 펜윅 트리
  tree = [0] * (N + 1)

  # 구간합 쿼리로 변환
  for x in range(N):
    print(query(tree, N) - query(tree, order[x]) + 1)
    update(tree, order[x], 1)
