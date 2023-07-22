import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
CORRECT, INCORRECT = 1, 0

def solve(N, adj, order):
  # 첫번째부터 pop하면서 비교하기 위함
  order.reverse()

  if order.pop() != 1:
    return INCORRECT

  queue = deque([1])

  visited = [False] * (N + 1)
  visited[1] = True

  while queue:
    node = queue.popleft()
    next_nodes = {next for next in adj[node] if not visited[next]}

    while next_nodes:
      next = order.pop()
      if next not in next_nodes:
        return INCORRECT

      visited[next] = True
      next_nodes.remove(next)
      queue.append(next)

  return CORRECT

if __name__ == '__main__':
  N = int(input())
  adj = [set() for _ in range(N + 1)]

  for _ in range(N - 1):
    P, Q = map(int, input().split())
    adj[P].add(Q)
    adj[Q].add(P)

  order = [*map(int, input().split())]
  print(solve(N, adj, order))
