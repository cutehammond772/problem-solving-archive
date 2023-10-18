import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def analyse(N, matrix):
  adj = [set() for _ in range(N)]
  degrees = [0] * N

  for p in range(N - 1):
    for q in range(p + 1, N):
      e1, e2 = matrix[p][q], matrix[q][p]

      if e1 == e2 == 'N':
        continue

      # 확정된 상황이 아니므로, 진입 차수에 반영하지 않는다.
      if e1 == e2 == 'Y':
        adj[p].add(q)
        adj[q].add(p)

      elif e1 == 'Y':
        adj[p].add(q)
        degrees[q] += 1

      elif e2 == 'Y':
        adj[q].add(p)
        degrees[p] += 1

  return degrees, adj

def solve(N, matrix):
  degrees, adj = analyse(N, matrix)
  visit = [False] * N

  # 위상 정렬의 시작점이 될 최상위 노드 후보이다.
  nodes = [x for x in range(N) if not degrees[x]]

  for root in nodes:
    if visit[root]: continue

    queue = deque([root])
    visit[root] = True

    while queue:
      node = queue.popleft()

      for next in adj[node]:
        # 양방향 간선에 의한 사이클을 방지하기 위해서이다.
        if visit[next]: continue

        # 양방향 간선인 경우 차수에 반영되지 않는 점을 고려한다.
        if node not in adj[next]:
          degrees[next] -= 1

        if not degrees[next]:
          visit[next] = True
          queue.append(next)

  # 모두 방문해야 사이클이 없는 것이다.
  return visit.count(True) == N

if __name__ == "__main__":
  N = int(input())
  matrix = [[*input()] for _ in range(N)]

  print("YES" if solve(N, matrix) else "NO")
