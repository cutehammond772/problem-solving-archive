import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def create_scc(N, graph):
  candidates = []
  sccIDs, discovered = [0] * (N + 1), [0] * (N + 1)
  sccID = nodeID = 1

  def create(node):
    nonlocal nodeID, sccID

    id = discovered[node] = nodeID
    nodeID += 1

    candidates.append(node)

    for next in graph[node]:
      if not discovered[next]:
        id = min(id, create(next))
      elif not sccIDs[next]:
        id = min(id, discovered[next])

    if id == discovered[node]:
      while candidates:
        top = candidates.pop()
        sccIDs[top] = sccID

        if top == node:
          break

      sccID += 1

    return id

  for node in range(1, N + 1):
    if not discovered[node]:
      create(node)

  return sccID, sccIDs

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
      x, y = map(int, input().split())

      graph[x].append(y)

    S, sccIDs = create_scc(N, graph)

    in_degree = [0] * S
    in_degree[0] = -1

    for node in range(1, N + 1):
      sccNode = sccIDs[node]

      for next in graph[node]:
        sccNext = sccIDs[next]

        if sccNode == sccNext:
          continue

        in_degree[sccNext] += 1

    print(in_degree.count(0))
