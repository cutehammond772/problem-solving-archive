import sys
input = sys.stdin.readline

NaN = 2 ** 63 - 1
N, M = int(input()), int(input())
matrix = [[NaN] * N for _ in range(N)]

for _ in range(M):
  x, y, r = map(int, input().split())
  matrix[x - 1][y - 1] = min(matrix[x - 1][y - 1], r)
  
for l in range(N):
  for x in range(N):
    for y in range(N):
      if x == y:
        continue
        
      matrix[x][y] = min(matrix[x][y], matrix[x][l] + matrix[l][y])

for x in range(N):
  for y in range(N):
    cost = matrix[x][y] if matrix[x][y] != NaN else 0
    print(cost, end=' ')
  print()