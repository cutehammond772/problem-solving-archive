N, M = map(int, input().split())
matrix = [[[0, 0] for _ in range(M)] for _ in range(N)]

# index for accumulation
W, B = 0, 1

for n in range(N):
  row = input()
  for m in range(M):
    ch = row[m]
    
    if ch == 'W':
      matrix[n][m][W], matrix[n][m][B] = 0, 1
    elif ch == 'B':
      matrix[n][m][W], matrix[n][m][B] = 1, 0

    if m > 0:
      matrix[n][m][W] += matrix[n][m - 1][B]
      matrix[n][m][B] += matrix[n][m - 1][W]

result = N * M

for n in range(N - 7):
  for m in range(M - 7):
    # start point is white, black
    w, b = 0, 0
    for x in range(8):
      P = B if x % 2 == 0 else W
      Q = W if x % 2 == 0 else B
      
      w += matrix[n + x][m + 7][P] - (matrix[n + x][m - 1][P] if m != 0 else 0)
      b += matrix[n + x][m + 7][Q] - (matrix[n + x][m - 1][Q] if m != 0 else 0)

    result = min(w, b, result)

print(result)