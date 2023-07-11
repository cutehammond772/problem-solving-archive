import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().strip()
NaN = 100000


def dijkstra(N, edges, P, Q):
  heap = []
  dist = [NaN] * N

  dist[P] = 0
  heappush(heap, (0, P))

  while heap:
    _, idx = heappop(heap)

    for edge in edges[idx]:
      next, cost = edge

      if dist[next] > dist[idx] + cost:
        dist[next] = dist[idx] + cost

        if next != Q:
          heappush(heap, (cost, next))

  return dist[Q]


if __name__ == '__main__':
  N, M, X = map(int, input().split())
  edges = [set() for _ in range(N)]

  for _ in range(M):
    P, Q, T = map(int, input().split())
    edges[P - 1].add((Q - 1, T))

  print(
    max([
      dijkstra(N, edges, t, X - 1) + dijkstra(N, edges, X - 1, t)
      for t in range(N)
    ]))
