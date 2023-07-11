import sys
input = lambda: sys.stdin.readline()

def find(U, x):
  if U[x] == x:
    return x

  mark = [x]
  
  while mark[-1] != U[mark[-1]]:
    mark.append(U[mark[-1]])

  for node in mark:
    U[node] = mark[-1]
    
  return U[x]

def union(U, x, y):
  x, y = find(U, x), find(U, y)
  
  if x == y:
    return

  if U[x] > U[y]:
    U[x] = U[y]
  else:
    U[y] = U[x]

def analyze(N, M, K, C):
  U = [x for x in range(N)]

  for _ in range(M):
    x, y = map(int, input().split())
    union(U, x - 1, y - 1)

  result = []
  accumulations = [0] * N
  counts = [0] * N
  
  for x in range(N):
    group = find(U, x)
      
    counts[group] += 1
    accumulations[group] += C[x]

  for x in range(N):
    if accumulations[x] == 0 or counts[x] >= K:
      continue

    result.append((counts[x], accumulations[x]))
    
  return result

def knapsack(C, E):
  result = 0
  matrix = [[0] * (C + 1) for _ in range(len(E) + 1)]
  
  for idx in range(len(E) + 1):
    for limit in range(C + 1):
      if idx == 0 or limit == 0:
        continue
        
      cost, value = E[idx - 1]
      
      if cost <= limit:
        matrix[idx][limit] = max(
          matrix[idx - 1][limit],
          matrix[idx - 1][limit - cost] + value
        )
      else:
        matrix[idx][limit] = matrix[idx - 1][limit]
        
      result = max(result, matrix[idx][limit])
      
  return result

if __name__ == '__main__':
  N, M, K = map(int, input().split())

  # 각 아이가 가지고 있는 사탕 수
  C = [*map(int, input().split())]
  
  # 각 그룹이 가지고 있는 사탕 수
  G = analyze(N, M, K, C)
  
  # K(명) 미만의 비용(친구)으로 얻을 수 있는 사탕의 수
  result = knapsack(K - 1, G)

  # 결과 출력
  print(result)