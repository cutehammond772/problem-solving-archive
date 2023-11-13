import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10

def dijkstra(n, s, graph):
  memo = [INF] * (n + 1)
  memo[s] = 0

  queue = [(0, s)]

  while queue:
    dist, node = heappop(queue)

    for next, cost in graph[node]:
      next_dist = dist + cost

      if memo[next] <= next_dist:
        continue

      memo[next] = next_dist
      heappush(queue, (next_dist, next))

  return memo

def solve(n, t, s, g, h, d0, graph, candidate):
  s_to = dijkstra(n, s, graph)
  g_to = dijkstra(n, g, graph)
  h_to = dijkstra(n, h, graph)

  result = []

  for i in range(t):
    c = candidate[i]

    # 실제 최단 경로이다.
    target = s_to[c]

    d1 = s_to[g] + d0 + h_to[c]
    d2 = s_to[h] + d0 + g_to[c]

    if min(d1, d2) == target:
      result.append(c)

  result.sort()
  return result

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    d0 = INF
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
      a, b, d = map(int, input().split())

      graph[a].append((b, d))
      graph[b].append((a, d))

      # (g, h) 사이의 길이
      if (a, b) == (g, h) or (a, b) == (h, g):
        d0 = d

    candidate = [int(input()) for _ in range(t)]
    result = solve(n, t, s, g, h, d0, graph, candidate)

    print(*result)
