import sys
from heapq import heappop, heapify
input = lambda: sys.stdin.readline().rstrip()

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

  if x > y:
    U[x] = U[y]
  else:
    U[y] = U[x]

def solve(N, edges):
  U = [x for x in range(N)]
  costs = []
  
  heapify(edges)
  
  while len(costs) != N - 1:
    cost, x, y = heappop(edges)
    
    if find(U, x) == find(U, y):
      continue
      
    costs.append(cost)
    union(U, x, y)
    
  return sum(costs) - max(costs)

if __name__ == '__main__':
  N, M = map(int, input().split())
  edges = []
  
  for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A - 1, B - 1))

  print(solve(N, edges))