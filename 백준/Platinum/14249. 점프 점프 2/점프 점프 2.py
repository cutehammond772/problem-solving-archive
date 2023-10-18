import sys
from collections import deque

sys.setrecursionlimit(150001)
input = lambda: sys.stdin.readline().rstrip()

def to_graph(N, A):
  adj = [[] for _ in range(N + 1)]

  for node in range(1, N + 1):
    left, right = node - A[node], node + A[node]

    if 1 <= left <= N:
      adj[node].append(left)

    if 1 <= right <= N:
      adj[node].append(right)

  return adj

def scc_groups(N, adj):
  nodeID, sccID = 1, 1
  discover, sccGroup = [0] * (N + 1), [0] * (N + 1)
  candidate = []

  def createSCC(node):
    nonlocal nodeID, sccID
    id = discover[node] = nodeID
    nodeID += 1

    candidate.append(node)

    for next in adj[node]:
      if not discover[next]: id = min(id, createSCC(next))
      elif not sccGroup[next]: id = min(id, discover[next])

    if id == discover[node]:
      while candidate:
        top = candidate.pop()
        sccGroup[top] = sccID

        if top == node:
          break

      sccID += 1

    return id

  for node in range(1, N + 1):
    if not discover[node]: createSCC(node)

  return sccID - 1, sccGroup

def scc_graph(scc, graph, group):
  sccGraph = [[] for _ in range(scc + 1)]
  cost = [0] * (scc + 1)

  # SCC를 노드로 하는 DAG를 생성한다.
  for node in range(1, N + 1):
    sccNode = group[node]
    cost[sccNode] += 1

    for next in graph[node]:
      sccNext = group[next]

      if sccNode == sccNext:
        continue

      sccGraph[sccNode].append(sccNext)

  return cost, sccGraph

def refine(scc, sccStart, sccGraph):
  # 시작점 S에서 방문할 수 있는 노드를 제외하고 모두 제거한다.
  graph = [[] for _ in range(scc + 1)]
  visit = [False] * (scc + 1)
  degrees = [0] * (scc + 1)

  queue = deque([sccStart])
  visit[sccStart] = True

  while queue:
    sccNode = queue.popleft()

    for sccNext in sccGraph[sccNode]:
      graph[sccNode].append(sccNext)
      degrees[sccNext] += 1

      if visit[sccNext]: continue
      visit[sccNext] = True

      queue.append(sccNext)

  return degrees, graph

def solve(N, A, S):
  # 사이클이 포함될 수 있는 일반 그래프이다.
  graph = to_graph(N, A)

  # SCC의 수와 노드가 속한 SCC 그룹을 나타낸다.
  scc, group = scc_groups(N, graph)

  # SCC를 노드로 하는 DAG를 생성한다.
  cost, sccGraph = scc_graph(scc, graph, group)

  # 시작점 S에서 방문할 수 있는 노드를 제외하고 모두 제거한다.
  degrees, refinedGraph = refine(scc, group[S], sccGraph)

  # 위상 정렬과 DP를 이용하여 방문 가능한 최대 돌의 개수를 구한다.
  memo = [0] * (scc + 1)
  sccStart = group[S]

  queue = deque([sccStart])
  memo[sccStart] = cost[sccStart]

  while queue:
    sccNode = queue.popleft()

    for sccNext in refinedGraph[sccNode]:
      memo[sccNext] = max(memo[sccNext], memo[sccNode] + cost[sccNext])
      degrees[sccNext] -= 1

      if not degrees[sccNext]:
        queue.append(sccNext)

  return max(memo)

if __name__ == "__main__":
  N = int(input())
  A = [0] + [*map(int, input().split())]
  S = int(input())

  print(solve(N, A, S))
