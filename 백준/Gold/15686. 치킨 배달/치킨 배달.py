import sys
input = lambda: sys.stdin.readline().rstrip()

CHICKEN, RESIDENT = 2, 1

def analyse(N, matrix):
  chickens, residents = [], []

  for row in range(N):
    for col in range(N):
      if matrix[row][col] == CHICKEN:
        chickens.append((row, col))

      if matrix[row][col] == RESIDENT:
        residents.append((row, col))

  return chickens, residents

def dist2(P, Q):
  return abs(P[0] - Q[0]) + abs(P[1] - Q[1])

def count(x):
  result = 0

  while x:
    result += x & 1

    x >>= 1

  return result

def solve(N, M, matrix):
  chickens, residents = analyse(N, matrix)
  C, R = len(chickens), len(residents)

  memo = [[dist2(chickens[x], residents[y]) for y in range(R)] for x in range(C)]
  result = 10 ** 10

  for bit in range(1, 1 << C):
    if count(bit) > M:
      continue

    total = 0

    for y in range(R):
      dist = 101

      for x in range(C):
        if not (bit & (1 << x)):
          continue

        dist = min(dist, memo[x][y])

      total += dist

    result = min(result, total)

  return result

if __name__ == "__main__":
  N, M = map(int, input().split())
  matrix = []

  for _ in range(N):
    matrix.append([*map(int, input().split())])

  print(solve(N, M, matrix))
