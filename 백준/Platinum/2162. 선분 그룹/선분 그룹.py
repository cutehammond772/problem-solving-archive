import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

def find(U, k):
  if U[k] == k:
    return k
    
  traversal = [k]
  
  while U[traversal[-1]] != traversal[-1]:
    traversal.append(U[traversal[-1]])
    
  for node in traversal:
    U[node] = traversal[-1]
    
  return U[k]

def union(U, x, y):
  x = find(U, x)
  y = find(U, y)
    
  if U[x] > U[y]:
    U[x] = U[y]
  else:
    U[y] = U[x]

def compare(x1, y1, x2, y2):
  if x1 == x2:
    return y2 - y1
    
  return x2 - x1

def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
  
  if result > 0:
    return 1

  if result < 0:
    return -1
    
  return 0

def intersects(L1, L2):
  x1, y1, x2, y2 = L1
  x3, y3, x4, y4 = L2

  P = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
  Q = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

  if P == Q == 0:
    if compare(x1, y1, x2, y2) < 0:
      x1, x2 = x2, x1
      y1, y2 = y2, y1
      
    if compare(x3, y3, x4, y4) < 0:
      x3, x4 = x4, x3
      y3, y4 = y4, y3
      
    return compare(x1, y1, x4, y4) >= 0 and compare(x3, y3, x2, y2) >= 0
  else:
    return P <= 0 and Q <= 0
  
if __name__ == '__main__':
  N = int(input())
  
  P = [tuple(map(int, input().split())) for _ in range(N)]
  U = [x for x in range(N)]

  for x, y in combinations(range(N), 2):
    if find(U, x) == find(U, y):
      continue
      
    if intersects(P[x], P[y]):
      union(U, x, y)

  U = [find(U, x) for x in range(N)]
  groups = set(U)
  print(len(groups))
  print(max([U.count(x) for x in groups]))