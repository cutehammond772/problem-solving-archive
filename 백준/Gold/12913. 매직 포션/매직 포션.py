import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 10

def convert(N, matrix):
  graph = [[] for _ in range(N)]

  for i in range(N - 1):
    for j in range(i + 1, N):
      graph[i].append((j, matrix[i][j]))
      graph[j].append((i, matrix[j][i]))

  return graph

# 0 -> 1 최단거리 구하기
def solve(N, K, matrix):
  graph = convert(N, matrix)

  memo = [[INF] * (K + 1) for _ in range(N)]
  queue = []

  # (distance, potions used, node)
  queue.append((0, 0, 0))
  memo[0][0] = 0

  while queue:
    dist, potions, node = heappop(queue)

    if dist > memo[node][potions]:
      continue

    for next, cost in graph[node]:
      next_dist, potion_dist = dist + cost, dist + (cost * 0.5)

      # 포션을 사용하지 않는 경우
      if next_dist < memo[next][potions]:
        memo[next][potions] = next_dist
        heappush(queue, (next_dist, potions, next))

      # 포션을 사용하는 경우
      if potions < K and potion_dist < memo[next][potions + 1]:
        memo[next][potions + 1] = potion_dist
        heappush(queue, (potion_dist, potions + 1, next))

  return min(memo[1])

if __name__ == '__main__':
  N, K = map(int, input().split())
  matrix = [[float(ch) for ch in input()] for _ in range(N)]

  print(solve(N, K, matrix))
