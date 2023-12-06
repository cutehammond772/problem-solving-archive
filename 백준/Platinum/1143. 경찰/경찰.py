import sys
input = lambda: sys.stdin.readline().rstrip()

def create_scc(N, G):
  sccID = nodeID = 1

  sccIDs, discover = [0] * N, [0] * N
  candidate = []

  def create(node):
    nonlocal sccID, nodeID

    id = discover[node] = nodeID
    candidate.append(node)

    nodeID += 1

    for next in G[node]:
      if not discover[next]: id = min(id, create(next))
      elif not sccIDs[next]: id = min(id, discover[next])

    if id == discover[node]:
      while candidate:
        top = candidate.pop()
        sccIDs[top] = sccID

        if top == node:
          break

      sccID += 1

    return id

  for node in range(N):
    if not discover[node]: create(node)

  in_degree = [0] * sccID
  sccNodes = [[] for _ in range(sccID)]

  for node in range(N):
    sccNodes[sccIDs[node]].append(node)

    for next in G[node]:
      if sccIDs[node] != sccIDs[next]:
        in_degree[sccIDs[next]] += 1

  sccRoots = [sccNode for sccNode in range(1, sccID) if in_degree[sccNode] == 0]

  return sccID, sccNodes, sccRoots

def solve(N, C, G):
  S, sccNodes, sccRoots = create_scc(N, G)

  # 총 비용, 경찰서의 수
  total, count = 0, 0

  # 해당 노드에 경찰서가 설치되었는지 체크한다.
  checked = [False] * N

  # 1. 각 루트 당 최소 노드를 먼저 하나씩 추가하여, 최소 조건을 만족한다.
  for sccRoot in sccRoots:
    min_node = min(sccNodes[sccRoot], key=lambda x: C[x])

    checked[min_node] = True

    total += C[min_node]
    count += 1

  # 2. 나머지 노드를 비용 순으로 정렬하여, 평균이 최소가 될 때까지 추가한다.
  last = [C[node] for node in range(N) if not checked[node]]
  last.sort(reverse=True)

  while last:
    cost = last.pop()
    next_avg = (total + cost) / (count + 1)

    if next_avg >= (total / count):
      break

    total += cost
    count += 1

  return total / count

if __name__ == "__main__":
  N = int(input())
  C = [*map(int, input().split())]

  M = [[*input()] for _ in range(N)]
  G = [[] for _ in range(N)]

  for i in range(N):
    for j in range(N):
      if M[i][j] == 'Y':
        G[i].append(j)

  print(solve(N, C, G))
