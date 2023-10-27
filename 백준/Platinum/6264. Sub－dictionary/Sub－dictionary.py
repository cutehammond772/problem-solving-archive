import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def create(N, adj):
  sccIDs = [0] * N
  discover = [0] * N

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

  for node in range(N):
    if not discover[node]:
      createSCC(node)

  return sccID - 1, sccIDs

def mapper():
  id, ids = 0, {}
  dictionary = []

  def convert(s):
    nonlocal id

    if s in ids:
      return ids[s]

    ids[s] = id
    id += 1

    dictionary.append(s)
    return ids[s]

  def get(i):
    return dictionary[i]

  def total():
    return id

  return convert, get, total

def solve(N, adj):
  result = []
  S, sccIDs = create(N, adj)

  indegree = [0] * (S + 1)
  sccGraph = [set() for _ in range(S + 1)]

  for node in range(N):
    sccNode = sccIDs[node]

    for next in adj[node]:
      sccNext = sccIDs[next]

      if sccNode == sccNext:
        continue

      if sccNext in sccGraph[sccNode]:
        continue

      sccGraph[sccNode].add(sccNext)
      indegree[sccNext] += 1

  queue = deque([(x, False) for x in range(1, S + 1) if not indegree[x]])

  while queue:
    sccNode, check = queue.popleft()
    nodes = []

    for node in range(N):
      if sccIDs[node] == sccNode:
        nodes.append(node)

    if len(nodes) > 1:
      check = True

    if check:
      result.extend(nodes)

    for sccNext in sccGraph[sccNode]:
      indegree[sccNext] -= 1

      if not indegree[sccNext]:
        queue.append((sccNext, check))

  return result

if __name__ == "__main__":
  while N := int(input()):
    convert, get, total = mapper()
    adj = [set() for _ in range(100)]

    for _ in range(N):
      A, *S = map(convert, input().split())

      for node in S:
        adj[A].add(node)

    result = [get(x) for x in solve(total(), adj)]
    result.sort()

    print(len(result))
    print(*result)
