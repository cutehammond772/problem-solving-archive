import sys, math
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def create(N, A):
  MAX_DEPTH = int(math.log2(40000)) + 1
  
  depths = [0] * (N + 1)
  distances = [0] * (N + 1)
  ancestor = [[0] * MAX_DEPTH for _ in range(N + 1)]
  
  # (depth, root, node)
  queue = deque([(1, 0, 1)])
  depths[1] = 1
  
  while queue:
    depth, root, node = queue.popleft()
    
    # 2^0번째 조상
    ancestor[node][0] = root
    
    # DP를 활용하여 2^N번째 조상 구하기
    for n in range(1, MAX_DEPTH):
      ancestor[node][n] = ancestor[ancestor[node][n - 1]][n - 1]
    
    for next, cost in A[node]:
      if next == root:
        continue
      
      depths[next] = depth + 1
      distances[next] = distances[node] + cost
      
      queue.append((depth + 1, node, next))
      
  def distance(X, Y):
    if depths[X] < depths[Y]:
      X, Y = Y, X
    
    start, dest = X, Y
    
    for idx in range(MAX_DEPTH - 1, -1, -1):
      if depths[ancestor[X][idx]] >= depths[Y]:
        X = ancestor[X][idx]
        
    if X == Y:
      return distances[start] - distances[dest]
    
    for idx in range(MAX_DEPTH - 1, -1, -1):
      if ancestor[X][idx] != ancestor[Y][idx]:
        X, Y = ancestor[X][idx], ancestor[Y][idx]
        
    intersection = ancestor[X][0]
    return (distances[start] - distances[intersection]) + (distances[dest] - distances[intersection])
  
  return distance

if __name__ == '__main__':
  N = int(input())
  A = [set() for _ in range(N + 1)]
  
  for _ in range(N - 1):
    P, Q, C = map(int, input().split())
    
    A[P].add((Q, C))
    A[Q].add((P, C))
  
  distance = create(N, A)
  M = int(input())
  
  for _ in range(M):
    X, Y = map(int, input().split())
    print(distance(X, Y))
    