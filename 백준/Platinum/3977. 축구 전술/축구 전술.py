import sys

sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def solve(N, G):
  sccIDs = [0] * N
  discover = [0] * N

  candidate = []
  sccID = nodeID = 1

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
        sccIDs[top := candidate.pop()] = sccID

        if top == node:
          break

      sccID += 1

    return id

  # 1. SCC 구성
  for node in range(N):
    if not discover[node]: create(node)

  # 2. InDegree = 0 인 SCC 노드 찾기
  in_degree = [0] * sccID

  for node in range(N):
    for next in G[node]:
      if sccIDs[node] == sccIDs[next]:
        continue

      in_degree[sccIDs[next]] += 1

  sccNodes = [sccNode for sccNode in range(1, sccID) if in_degree[sccNode] == 0]

  # 3. 시작 구역 체크
  if len(sccNodes) != 1:
    return []

  else:
    sccTarget = sccNodes[0]

    return [node for node in range(N) if sccIDs[node] == sccTarget]

if __name__ == "__main__":
  T = int(input())

  for t in range(T):
    # 빈 줄 구분
    if t > 0: input()

    N, M = map(int, input().split())
    G = [[] for _ in range(N)]

    for _ in range(M):
      A, B = map(int, input().split())
      G[A].append(B)

    result = solve(N, G)

    if result:
      print(*result, sep='\n')

    else:
      print("Confused")

    # 빈 줄 출력
    if t < T - 1: print()
    