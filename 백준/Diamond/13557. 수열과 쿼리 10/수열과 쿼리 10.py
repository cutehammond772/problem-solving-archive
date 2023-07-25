import sys, math
input = lambda: sys.stdin.readline().rstrip()

# 최대 부분 합 트리
def create(N, A):
  L = 2 ** (math.ceil(math.log2(N)) + 1)

  # 특정 구간에서, [맨 좌측 원소 포함, 맨 우측 원소 포함, 최대 부분합, 전체 합]
  tree = [[0] * 4 for _ in range(L)]

  def make(node, left, right):
    if left == right:
      tree[node] = [A[left]] * 4
      return

    mid = (left + right) // 2
    make(node * 2, left, mid)
    make(node * 2 + 1, mid + 1, right)

    LN, RN = tree[node * 2], tree[node * 2 + 1]

    tree[node] = [
      max(LN[0], LN[3] + RN[0]),
      max(RN[1], LN[1] + RN[3]),
      max(LN[2], RN[2], LN[1] + RN[0]),
      LN[3] + RN[3]
    ]

  make(1, 0, N - 1)
  return tree

def query(N, tree, x, y):
  def recursion(node, left, right):
    if left > y or right < x:
      return None

    if x <= left and right <= y:
      return tree[node]

    mid = (left + right) // 2
    LN = recursion(node * 2, left, mid)
    RN = recursion(node * 2 + 1, mid + 1, right)

    if not LN:
      return RN

    if not RN:
      return LN

    return [
      max(LN[0], LN[3] + RN[0]),
      max(RN[1], LN[1] + RN[3]),
      max(LN[2], RN[2], LN[1] + RN[0]),
      LN[3] + RN[3]
    ]

  return recursion(1, 0, N - 1)

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  tree = create(N, A)
  M = int(input())

  for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

    # Case 1. 두 i, j 구간이 겹치지 않는 경우
    if y1 < x2:
      result = 0

      # [x1, y1] 구간에서 y1를 포함하는 최대 부분합
      result += query(N, tree, x1, y1)[1]

      # [x2, y2] 구간에서 x2를 포함하는 최대 부분합
      result += query(N, tree, x2, y2)[0]

      # 중간 구간
      if y1 + 1 <= x2 - 1:
        result += query(N, tree, y1 + 1, x2 - 1)[3]

    # Case 2. 전체 구간을 네 구간으로 나눌 수 있을 때
    elif x1 < x2 and y1 < y2:
      c1 = query(N, tree, x2, y1)[2]
      c2 = query(N, tree, x1, x2)[1] + query(N, tree, x2, y2)[0] - A[x2]
      c3 = query(N, tree, x1, y1)[1] + query(N, tree, y1, y2)[0] - A[y1]
      result = max(c1, c2, c3)

    # Case 3. 전체 구간을 세 구간으로 나눌 수 있을 때
    elif x1 == x2 and y1 < y2:
      c1 = query(N, tree, x1, y1)[2]
      c2 = query(N, tree, x1, y1)[1] + query(N, tree, y1, y2)[0] - A[y1]
      result = max(c1, c2)

    elif x1 < x2 and y1 == y2:
      c1 = query(N, tree, x2, y2)[2]
      c2 = query(N, tree, x1, x2)[1] + query(N, tree, x2, y2)[0] - A[x2]
      result = max(c1, c2)

    # Case 4. i, j 구간이 동일한 경우
    else:
      result = query(N, tree, x1, y1)[2]

    print(result)
