import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
NaN = 100000 * 999 + 1

def solve(matrix, start, dest, N):
  heap = []
  dist = [NaN] * N
  
  # 시작점 초기화
  dist[start] = 0
  heappush(heap, (0, start))

  # 다익스트라 수행
  while heap:
    _, node = heappop(heap)

    for i in range(N):
      cost = matrix[node][i]
        
      if dist[i] > dist[node] + cost:
        dist[i] = dist[node] + cost
        heappush(heap, (cost, i))

  return dist[dest]

if __name__ == '__main__':
  N = int(input())
  M = int(input())

  matrix = [[NaN] * N for _ in range(N)]

  # 비용 설정
  for _ in range(M):
    start, dest, cost = map(int, input().split())
    matrix[start - 1][dest - 1] = min(matrix[start - 1][dest - 1], cost)

  # 시작점, 도착점
  start, dest = map(int, input().split())
  result = solve(matrix, start - 1, dest - 1, N)
  print(result)