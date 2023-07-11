import sys
from heapq import heappush, heappop
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

def distance(x1, y1, x2, y2):
  return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def solve(N, V, E):
  result = 0
  vertices = { 0 }
  queue = []

  for edge in E[0]:
    heappush(queue, edge)

  while queue and len(vertices) < N:
    dist, next = heappop(queue)
    
    if next in vertices:
      continue

    vertices.add(next)
    result += dist

    for edge in E[next]:
      if edge[1] not in vertices:
        heappush(queue, edge)
      
  return result

if __name__ == '__main__':
  N = int(input())
  V = [tuple(map(float, input().split())) for _ in range(N)]
  E = [[] for _ in range(N)]
  
  for p, q in combinations(range(N), 2):
    dist = distance(*V[p], *V[q])
    E[p].append((dist, q))
    E[q].append((dist, p))

  print('{:.2f}'.format(solve(N, V, E)))