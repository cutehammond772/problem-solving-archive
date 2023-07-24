import sys
input = lambda: sys.stdin.readline().rstrip()
MODIFY, SUM = 1, 2

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
  A = [*map(int, input().split())]

  tree = [0] * (N + 1)

  # 펜윅 트리 초기화
  for x in range(N):
    update(tree, x + 1, A[x])

  # 오프라인 쿼리
  M = int(input())

  # 변경 쿼리, 합 쿼리
  MQ, SQ = [], []

  for _ in range(M):
    command, *args = map(int, input().split())

    if command == MODIFY:
      MQ.append(args)

    elif command == SUM:
      SQ.append(args + [len(SQ)])

  # 변경 쿼리의 순서에 따라 합 쿼리를 정렬
  SQ.sort()

  result = [0] * len(SQ)
  mod_order = 0

  for x in range(len(SQ)):
    k, i, j, result_idx = SQ[x]

    # 변경 쿼리 대상이 바뀌었을 때
    if mod_order != k:
      for t in range(mod_order, k):
        mi, mv = MQ[t]

        diff = mv - A[mi - 1]
        update(tree, mi, diff)
        A[mi - 1] = mv

      mod_order = k

    result[result_idx] = query(tree, j) - query(tree, i - 1)

  print(*result, sep='\n')
