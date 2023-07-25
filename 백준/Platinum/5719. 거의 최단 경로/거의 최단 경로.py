import sys
from heapq import heappush, heappop
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10 + 1

def dijkstra(N, adj, costs, x, y):
  dist = [INF] * N
  routes = [set() for _ in range(N)]

  heap = []

  dist[x] = 0
  heappush(heap, (0, x))

  while heap:
    _, node = heappop(heap)

    for next in adj[node]:
      cost = costs[node][next]

      if dist[next] < dist[node] + cost:
        continue

      if dist[next] > dist[node] + cost:
        routes[next].clear()
        heappush(heap, (cost, next))

      routes[next].add(node)
      dist[next] = dist[node] + cost

  return routes, dist[y]

def shortest(N, adj, costs, S, D):
  routes, dist = dijkstra(N, adj, costs, S, D)

  if dist == INF:
    return -1

  queue = deque()
  visited = [False] * N

  queue.append(D)
  visited[D] = True

  while queue:
    node = queue.popleft()

    for previous in routes[node]:
      adj[previous].remove(node)

      if visited[previous]:
        continue

      visited[previous] = True
      queue.append(previous)

  return dist

if __name__ == '__main__':
  while True:
    N, M = map(int, input().split())

    if N == M == 0:
      break

    S, D = map(int, input().split())
    adj = [set() for _ in range(N)]
    costs = [[0] * N for _ in range(N)]

    for _ in range(M):
      U, V, P = map(int, input().split())

      adj[U].add(V)
      costs[U][V] = P

    # shortest distance
    dist = shortest(N, adj, costs, S, D)

    if dist == -1:
      print(-1)
      continue

    # second-shortest distance
    result = dijkstra(N, adj, costs, S, D)[1]
    print(result if result != INF else -1)
