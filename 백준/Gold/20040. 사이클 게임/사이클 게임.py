import sys
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

  if U[x] > U[y]:
    U[x] = U[y]
  else:
    U[y] = U[x]

def solve(N, M, edges):
  U = [x for x in range(N)]
  
  for t in range(M):
    x, y = edges[t]
    
    if find(U, x) == find(U, y):
      return t + 1

    union(U, x, y)
    
  return 0

if __name__ == '__main__':
  N, M = map(int, input().split())
  edges = []

  for _ in range(M):
    P, Q = map(int, input().split())
    edges.append((P, Q))

  print(solve(N, M, edges))