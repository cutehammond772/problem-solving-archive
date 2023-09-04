import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

# -> 최종 난이도를 기준으로 minheap을 돌린다.
# (증명) 특정 몬스터 a의 난이도 하락에 b가 필요할 때,
# (a) b >= a 이면 b를 잡아도 이득이 되지 않는다.
# - 왜냐하면, b를 잡는 경우 최대 난이도는 b이기 때문이다.
# (b) b < a 이면 몬스터 b를 먼저 잡는 것이 이득이다.
# - b를 먼저 잡은 다음, 하락한 난이도를 반영한 a를 다시 minheap에 넣으면 된다.
if __name__ == '__main__':
  N, M = map(int, input().split())
  C = [0] + [*map(int, input().split())]
  T = [[] for _ in range(N + 1)]
  P = int(input())

  for _ in range(P):
    a, b, t = map(int, input().split())
    T[a].append((b, t))
    C[b] += t

  queue = [(C[x], x) for x in range(1, N + 1)]
  checked = [False] * (N + 1)

  result, count = 0, 0
  heapify(queue)

  while queue and count < M:
    cost, idx = heappop(queue)

    if checked[idx]:
      continue

    result = max(result, cost)
    checked[idx] = True
    count += 1

    if len(T[idx]):
      for node, discount in T[idx]:
        C[node] -= discount
        heappush(queue, (C[node], node))

  print(result)
