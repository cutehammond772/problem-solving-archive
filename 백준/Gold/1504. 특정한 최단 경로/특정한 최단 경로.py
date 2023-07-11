import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
NaN = 799 * 1000 + 1

def dijkstra(N, edges, P, Q):
  if P == Q:
    return 0
    
  heap = []
  dist = [NaN] * N

  dist[P] = 0
  heappush(heap, (0, P))

  while heap:
    _, idx = heappop(heap)

    for edge in edges[idx]:
      cost, next = edge

      if dist[next] > dist[idx] + cost:
        dist[next] = dist[idx] + cost

        if next != Q:
          heappush(heap, (cost, next))

  return dist[Q]


if __name__ == '__main__':
  N, E = map(int, input().split())
  edges = [set() for _ in range(N)]

  for _ in range(E):
    P, Q, C = map(int, input().split())
    edges[P - 1].add((C, Q - 1))
    edges[Q - 1].add((C, P - 1))

  V1, V2 = map(int, input().split())

  # V1부터 V2까지의 최단거리
  v1_v2 = dijkstra(N, edges, V1 - 1, V2 - 1)
  
  # 1부터 V1까지의 최단거리
  start_to_v1 = dijkstra(N, edges, 0, V1 - 1)

  # 1부터 V2까지의 최단거리
  start_to_v2 = dijkstra(N, edges, 0, V2 - 1)
  
  # V1부터 N까지의 최단거리
  v1_to_dest = dijkstra(N, edges, V1 - 1, N - 1)

  # V2부터 N까지의 최단거리
  v2_to_dest = dijkstra(N, edges, V2 - 1, N - 1)

  result = NaN * 3
  
  # 케이스 1: [1 -> V1 -> V2 -> N]
  result_v1_v2 = [start_to_v1, v1_v2, v2_to_dest]
  if NaN not in result_v1_v2:
    result = min(result, sum(result_v1_v2))
    
  # 케이스 2: [1 -> V2 -> V1 -> N]
  result_v2_v1 = [start_to_v2, v1_v2, v1_to_dest]
  if NaN not in result_v2_v1:
    result = min(result, sum(result_v2_v1))  

  print(result if result != 3 * NaN else -1)
