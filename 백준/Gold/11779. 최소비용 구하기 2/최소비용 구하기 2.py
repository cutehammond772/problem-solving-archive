import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()
NaN = 100000 * 999 + 1

def solve(matrix, start, dest, N):
  heap = []
  dist = [NaN] * N
  mark = [NaN] * N
  
  # 시작점 초기화
  dist[start] = 0
  heappush(heap, (0, start))

  # 다익스트라 수행
  while heap:
    _, node = heappop(heap)

    for i in range(N):
      cost = matrix[node][i]
        
      if dist[i] > dist[node] + cost:
        # 더 최단거리일 때만 노드를 추가
        dist[i] = dist[node] + cost
        mark[i] = node
        heappush(heap, (cost, i))

  temp = mark[dest]
  result = [dest + 1]
  
  while temp != NaN:
    result.append(temp + 1)
    temp = mark[temp]
    
  return dist[dest], len(result), reversed(result)

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
  dist, count, result = solve(matrix, start - 1, dest - 1, N)
  
  print(dist)
  print(count)
  print(*result)
