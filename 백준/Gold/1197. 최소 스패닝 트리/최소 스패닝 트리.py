import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

def union_find(union, node):
  roots = [node]

  # 루트 노드까지 순회한다.
  while union[roots[-1]] != roots[-1]:
    roots.append(union[roots[-1]])

  # 중간 노드들을 모두 갱신한다.
  for x in roots:
    union[x] = roots[-1]
    
  # 루트 노드를 나타낸다.
  return roots[-1]

def solve(V, edges):
  queue = []
  union = [x for x in range(V)]
  count, result = 0, 0
  
  # 한 정점을 시작점으로 한다.
  for edge in edges[0]:
    heappush(queue, edge)

  # 간선이 V - 1개이면 MST가 형성된다.
  while count != V - 1:
    cost, node, next = heappop(queue)

    # 루트 노드가 같은지 체크한다.
    if union_find(union, node) == union_find(union, next):
      continue

    # 동일한 루트 노드를 갖도록 한다. (중간 노드의 갱신은 추후 이루어진다.)
    union[next] = union[node]
    
    # 트리에 추가한다.
    result += cost
    count += 1
    
    # '새로 추가된 노드'와 연결된 간선을 추가한다.
    for edge in edges[next]:
      heappush(queue, edge)
    
  return result

if __name__ == '__main__':
  V, E = map(int, input().split())
  edges = [[] for _ in range(V)]
  
  for _ in range(E):
    A, B, C = map(int, input().split())
    
    # (cost, node, next)
    edges[A - 1].append((C, A - 1, B - 1))
    edges[B - 1].append((C, B - 1, A - 1))
    
  print(solve(V, edges))