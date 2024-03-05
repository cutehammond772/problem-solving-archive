import sys
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

# Union Find Template (by Jungheon Lee)
def find(U, x):
  if U[x] == x:
    return U[x]

  nodes = [x]

  while U[nodes[-1]] != nodes[-1]:
    nodes.append(U[nodes[-1]])

  for node in nodes:
    U[node] = nodes[-1]

  return U[x]

def union(U, C, x, y):
  x, y = find(U, x), find(U, y)

  if x == y:
    return

  if C[x] < C[y]:
    x, y = y, x

  U[y] = U[x]
  C[x] += C[y]

def analyse(N, M, data):
  checked = [[False] * M for _ in range(N)]
  edges = []

  for row in range(N):
    for col in range(M):
      # 중복된 간선의 생성을 방지한다.
      checked[row][col] = True

      for x in range(0, 4):
        nrow, ncol = row + dr[x], col + dc[x]

        if not (0 <= nrow < N and 0 <= ncol < M):
          continue

        if checked[nrow][ncol]:
          continue

        # 두 높이 중 높은 쪽을 간선의 비용으로 정한다.
        edges.append((max(data[row][col], data[nrow][ncol]), row * M + col, nrow * M + ncol))

  return edges

def solve(N, edges, queries):
  E, Q = len(edges), len(queries)

  result = [0] * Q
  left, right = [0] * Q, [E] * Q

  edges.sort()

  while True:
    U, C = [*range(N)], [1] * N
    pbs = [[] for _ in range(E + 1)]
    count = 0

    for i in range(Q):
      if left[i] == right[i]:
        continue

      pbs[(left[i] + right[i]) >> 1].append(i)
      count += 1

    if not count:
      break

    for i in range(E):
      w, a, b = edges[i]
      union(U, C, a, b)

      for j in pbs[i]:
        x, y = queries[j]

        if find(U, x) == find(U, y):
          result[j], right[j] = w, i
        else:
          left[j] = i + 1

  return result

if __name__ == "__main__":
  N, M, Q = map(int, input().split())

  # 그래프 모델링
  data = [[*map(int, input().split())] for _ in range(N)]
  edges = analyse(N, M, data)

  # 쿼리 변환
  queries = []

  for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    u, v = (x1 - 1) * M + (y1 - 1), (x2 - 1) * M + (y2 - 1)

    queries.append((u, v))

  result = solve(N * M, edges, queries)

  for i in range(Q):
    u, v = queries[i]

    # 위치가 동일한 경우, 해당 위치의 높이가 최소이다.
    if u == v:
      result[i] = data[u // M][u % M]

    print(result[i])
