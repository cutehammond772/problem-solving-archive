import sys
sys.setrecursionlimit(10 ** 5 + 1)
input = lambda: sys.stdin.readline().rstrip()

ADJ, REV = 0, 1

def dfs(visited, adjacent, stack, node):
  visited[node] = True
  
  for next in adjacent[node]:
    if visited[next]:
      continue
      
    dfs(visited, adjacent, stack, next)

  stack.append(node)

# 코사라주 알고리즘 사용
def solve(V, adjacent, reversed):
  result, stack = [], []
  visited = [[False] * (V + 1) for _ in range(2)]

  # 정방향 그래프에 대해 DFS 수행
  for x in range(1, V + 1):
    if visited[ADJ][x]:
      continue
      
    dfs(visited[ADJ], adjacent, stack, x)
  
  # 역방향 그래프를 사용하여 SCC 생성
  while stack:
    x = stack.pop()

    if visited[REV][x]:
      continue
      
    component = []
    dfs(visited[REV], reversed, component, x)

    component.sort()
    component.append(-1)
    
    result.append(component)

  result.sort(key = lambda x: x[0])
  return result

if __name__ == '__main__':
  V, E = map(int, input().split())
  
  adjacent = [[] for _ in range(V + 1)]
  reversed = [[] for _ in range(V + 1)]
  
  for _ in range(E):
    P, Q = map(int, input().split())
    adjacent[P].append(Q)
    reversed[Q].append(P)

  components = solve(V, adjacent, reversed)
  print(len(components))
  
  for component in components:
    print(*component)