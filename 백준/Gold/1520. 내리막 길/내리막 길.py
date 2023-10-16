import sys
sys.setrecursionlimit(10 ** 5)

input = lambda: sys.stdin.readline().rstrip()
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(N, M, matrix):
  discovered = [[-1] * M for _ in range(N)]
  discovered[N - 1][M - 1] = 1

  def find(row, col):
    result = 0

    for x in range(4):
      nrow, ncol = row + dr[x], col + dc[x]

      if not (0 <= nrow < N and 0 <= ncol < M):
        continue

      if matrix[row][col] <= matrix[nrow][ncol]:
        continue
      
      if discovered[nrow][ncol] >= 0:
        result += discovered[nrow][ncol]
      else:
        result += find(nrow, ncol)

    discovered[row][col] = result
    return discovered[row][col]

  return find(0, 0)

if __name__ == "__main__":
  N, M = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  print(solve(N, M, matrix))
