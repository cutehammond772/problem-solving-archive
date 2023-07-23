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

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N, M = map(int, input().split())
    result = []

    tree = [0] * (N + M + 1)
    indexes = [0] * (N + M + 1)

    # 초기 설정
    for x in range(N):
      indexes[N - x] = (x + 1)
      update(tree, x + 1, 1)

    watch = [*map(int, input().split())]
    top = N

    for num in watch:
      index = indexes[num]

      # 위에 있는 DVD의 수
      result.append(query(tree, N + M) - query(tree, index))

      # DVD 위치 갱신
      top += 1

      indexes[num] = top
      update(tree, index, -1)
      update(tree, top, 1)

    print(*result)
