import sys
input = lambda: sys.stdin.readline().rstrip()

# 좌표 압축
def compress(N, C):
  indexes = sorted(range(N), key=lambda x: C[x][1])
  order, previous = 0, 10 ** 9 + 1

  for idx in indexes:
    if previous != C[idx][1]:
      order += 1

    previous = C[idx][1]
    C[idx][1] = order

  return order

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

# 펜윅 트리 이용
def solve(N, C):
  result = 0
  tree = [0] * ((L := compress(N, C)) + 1)

  for k in range(N):
    result += query(tree, L) - query(tree, C[k][1] - 1)
    update(tree, C[k][1], 1)

  return result

if __name__ == '__main__':
  T = int(input())
  for _ in range(T):
    N = int(input())

    # x값 오름차순, y값 내림차순으로 좌표 정렬
    C = [[*map(int, input().split())] for _ in range(N)]
    C.sort(key=lambda k: (k[0], -k[1]))

    print(solve(N, C))
