import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, matrix):
  result = 0

  for row in range(N):
    grundy = matrix[row][-1]

    for col in range(M - 2, -1, -1):
      next_grundy = matrix[row][col] - 1
      grundy = next_grundy + (grundy <= next_grundy)

    result ^= grundy

  return result

if __name__ == "__main__":
  N, M = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  result = solve(N, M, matrix)

  if result: print("koosaga")
  else: print("cubelover")
