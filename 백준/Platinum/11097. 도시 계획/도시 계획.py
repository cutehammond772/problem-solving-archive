import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 301

def create(N, adj):
  sccIDs = [0] * (N + 1)
  discover = [0] * (N + 1)

  candidate = []
  nodeID, sccID = 1, 1

  def createSCC(node):
    nonlocal nodeID, sccID

    id = discover[node] = nodeID
    candidate.append(node)
    nodeID += 1

    for next in adj[node]:
      if not discover[next]:
        id = min(id, createSCC(next))
      elif not sccIDs[next]:
        id = min(id, discover[next])

    if id == discover[node]:
      while candidate:
        top = candidate.pop()
        sccIDs[top] = sccID

        if top == node:
          break

      sccID += 1

    return id

  for node in range(1, N + 1):
    if not discover[node]:
      createSCC(node)

  return sccID - 1, sccIDs

def solve(N, adj):
  result = []

  S, sccIDs = create(N, adj)
  group = [[] for _ in range(S + 1)]

  dist = [[INF] * (S + 1) for _ in range(S + 1)]
  match = [[None] * (S + 1) for _ in range(S + 1)]

  for node in range(1, N + 1):
    sccNode = sccIDs[node]
    group[sccNode].append(node)

    for next in adj[node]:
      sccNext = sccIDs[next]

      if sccNode == sccNext:
        continue

      dist[sccNode][sccNext] = -1
      match[sccNode][sccNext] = (node, next)

  for nodes in group:
    if len(nodes) < 2:
      continue

    for x in range(len(nodes)):
      result.append((nodes[x - 1], nodes[x]))

  for k in range(1, S + 1):
    for i in range(1, S + 1):
      for j in range(1, S + 1):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  for node in range(1, S + 1):
    for next in range(1, S + 1):
      if dist[node][next] == -1:
        result.append(match[node][next])

  return result

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    # 빈 줄
    input()

    N = int(input())
    adj = [[] for _ in range(N + 1)]

    for a in range(1, N + 1):
      data = '0' + input()

      for b in range(1, N + 1):
        if a == b:
          continue

        if data[b] == '1':
          adj[a].append(b)

    result = solve(N, adj)

    print(len(result))
    for a, b in result:
      print(a, b)

    print()
