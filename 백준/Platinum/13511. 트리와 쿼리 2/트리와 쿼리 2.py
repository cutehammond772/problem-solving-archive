import sys, math
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def analysis(N, adj):
  D = math.ceil(math.log2(N)) + 1
  
  depths = [0] * (N + 1)
  distances = [0] * (N + 1)
  ancestors = [[0] * D for _ in range(N + 1)]
  
  queue = deque([(0, 1)])
  depths[1] = 1
  
  while queue:
    prev, node = queue.popleft()
    
    depth = depths[node]
    dist = distances[node]
    
    # 조상 설정
    ancestors[node][0] = prev
    
    for k in range(1, D):
      ancestors[node][k] = ancestors[ancestors[node][k - 1]][k - 1]
    
    # 하위 노드
    for next, cost in adj[node]:
      if prev == next:
        continue
      
      depths[next] = depth + 1
      distances[next] = dist + cost
      
      queue.append((node, next))
  
  # 최소 공통 조상 구하기
  def lca(A, B):
    if depths[A] < depths[B]:
      A, B = B, A
    
    for idx in range(D - 1, -1, -1):
      if depths[ancestors[A][idx]] < depths[B]:
        continue
      
      A = ancestors[A][idx]
    
    if A == B:
      return A
    
    for idx in range(D - 1, -1, -1):
      if ancestors[A][idx] == ancestors[B][idx]:
        continue
      
      A, B = ancestors[A][idx], ancestors[B][idx]
    
    return ancestors[A][0]
  
  # A -> C
  def kth(A, C, K):
    T = depths[C] + K
    
    for idx in range(D - 1, -1, -1):
      if depths[ancestors[A][idx]] < T:
        continue
      
      A = ancestors[A][idx]
    
    return A
  
  def distance(A, B):
    Da, Db = distances[A], distances[B]
    Dk = distances[lca(A, B)]
    
    return (Da - Dk) + (Db - Dk)
  
  def vertex(A, B, K):
    C = lca(A, B)
    Da, Db, Dc = depths[A], depths[B], depths[C]
    
    K -= 1
    diff = Da - Dc
    
    if diff >= K:
      return kth(A, C, diff - K)
    
    return kth(B, C, K - diff)
  
  return distance, vertex

if __name__ == '__main__':
  # 트리 전처리 (분석)
  N = int(input())
  adj = [set() for _ in range(N + 1)]
  
  for _ in range(N - 1):
    P, Q, C = map(int, input().split())
    
    adj[P].add((Q, C))
    adj[Q].add((P, C))
  
  distance, vertex = analysis(N, adj)
  
  # 쿼리 처리하기
  M = int(input())
  
  for _ in range(M):
    command, *args = map(int, input().split())
    
    if command == 1:
      print(distance(*args))
    
    elif command == 2:
      print(vertex(*args))
