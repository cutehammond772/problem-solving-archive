import sys
from math import log2, floor

input = lambda: sys.stdin.readline().rstrip()

INF = 0
MAX_DEPTH = floor(log2(100000)) + 1
                  
def preprocess(N):
  # (depth, adjacent)
  adj = [[] for _ in range(N + 1)]

  depth = [INF] * (N + 1)
  parent = [[INF] * MAX_DEPTH for _ in range(N + 1)]
  
  # 트리 생성
  for _ in range(N - 1):
    P, Q = map(int, input().split())

    # 아직 어느 노드가 부모 노드인지 알 수 없다.
    adj[Q].append(P)
    adj[P].append(Q)

  # 뎁스 설정
  stack = [(1, 1, 1)]

  while stack:
    # (현재 depth, 이전 노드, 현 노드)
    curdepth, previous, node = stack.pop()
    depth[node] = curdepth

    # 조상 노드 초기화
    parent[node][0] = previous
    for k in range(1, MAX_DEPTH):
      parent[node][k] = parent[parent[node][k - 1]][k - 1]
    
    for next in adj[node]:
      # 부모 노드를 향하는 경우 제외
      if next == previous:
        continue
        
      stack.append((curdepth + 1, node, next))

  return parent, depth

def solve(parent, depth, P, Q):
  if P == Q:
    return P
    
  if depth[P] < depth[Q]:
    P, Q = Q, P

  # depth 맞추기
  for x in range(MAX_DEPTH - 1, -1, -1):
    if depth[parent[P][x]] >= depth[Q]:
      P = parent[P][x]

  if P == Q:
    return P
    
  # 거슬러 올라가기
  for x in range(MAX_DEPTH - 1, -1, -1):
    if parent[P][x] != parent[Q][x]:
      P = parent[P][x]
      Q = parent[Q][x]
      
  return parent[P][0]
  
if __name__ == '__main__':
  N = int(input())
  parent, depth = preprocess(N)

  M = int(input())
  
  for _ in range(M):
    P, Q = map(int, input().split())
    print(solve(parent, depth, P, Q))