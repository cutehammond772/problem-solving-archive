import sys
from heapq import heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

def preprocess(N, P):
  edges = []
  
  # 각 직선 좌표에 대한 최단거리에 대한 간선을 저장한다.
  for w in range(3):
    adj = sorted([(P[x][w], x) for x in range(N)])
    
    for x in range(N - 1):
      curr, next = adj[x], adj[x + 1]
      
      # 양방향 간선을 제공한다.
      edges.append((next[0] - curr[0], curr[1], next[1]))
      edges.append((next[0] - curr[0], next[1], curr[1]))
      
  heapify(edges)
  return edges

def find(U, x):
  if U[x] == x:
    return U[x]

  traversal = [x]
  
  while U[traversal[-1]] != traversal[-1]:
    traversal.append(U[traversal[-1]])

  for node in traversal:
    U[node] = traversal[-1]
    
  return U[x]
    
def union(U, x, y):
  x, y = find(U, x), find(U, y)
  if x == y:
    return

  if U[x] > U[y]:
    U[x] = U[y]
  else:
    U[y] = U[x]
    
def solve(N, P):
  result = 0
  count = 0
  
  edges = preprocess(N, P)
  U = [x for x in range(N)]
  
  while edges and count < N - 1:
    C, A, B = heappop(edges)
    
    if find(U, A) == find(U, B):
      continue

    union(U, A, B)
    result += C
    count += 1
    
  return result

if __name__ == '__main__':
  N = int(input())
  P = [tuple(map(int, input().split())) for _ in range(N)]
  
  print(solve(N, P))