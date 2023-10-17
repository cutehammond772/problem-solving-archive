import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, matrix, off):
  result = 0

  def check(row, col, l, r, count):
    nonlocal result

    if row == N:
      result = max(result, count)
      return

    for next in range(col, N, 2):
      if matrix[row][next] == 0 or ((l | r) & 1 << next):
        continue

      check(row, next + 2, l | 1 << next, r | 1 << next, count + 1)

    check(row + 1, (off + (row + 1)) % 2, l >> 1, r << 1, count)

  check(0, off, 0, 0, 0)
  return result

if __name__ == "__main__":
  N = int(input())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  print(solve(N, matrix, 0) + solve(N, matrix, 1))
