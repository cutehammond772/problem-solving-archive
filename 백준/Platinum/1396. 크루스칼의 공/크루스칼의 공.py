import sys
input = lambda: sys.stdin.readline().rstrip()

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

def solve(N, M, Q, edges, queries):
  # 각 쿼리에 대한 결과
  result = [[0, 0] for _ in range(Q)]

  # Parallel Binary Search
  left, right = [0] * Q, [M] * Q

  # MST 구성을 위해 미리 정렬한다.
  edges.sort()

  while True:
    # Union-Find
    U, C = [*range(N + 1)], [1] * (N + 1)

    pbs = [[] for _ in range(M + 1)]
    count = 0

    # 각 mid 위치에 대상 쿼리를 추가
    for i in range(Q):
      if left[i] == right[i]:
        continue

      pbs[(left[i] + right[i]) >> 1].append(i)
      count += 1

    # 처리할 쿼리가 없는 경우
    if not count:
      break

    for i in range(M):
      # i번째 간선을 반영한다.
      c, a, b = edges[i]
      union(U, C, a, b)

      for j in pbs[i]:
        x, y = queries[j]

        if find(U, x) == find(U, y):
          result[j] = [c, C[find(U, x)]]
          right[j] = i

        else:
          left[j] = i + 1

  return result

if __name__ == "__main__":
  N, M = map(int, input().split())
  edges, queries = [], []

  for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

  Q = int(input())

  for _ in range(Q):
    x, y = map(int, input().split())
    queries.append((x, y))

  result = solve(N, M, Q, edges, queries)

  for c, v in result:
    if v == 0:
      print(-1)
    else:
      print(c, v)
