import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, matrix, elements):
  # [value, elements]
  dist = [[(0, 0) for _ in range(N + 1)] for _ in range(N + 1)]

  for r in range(1, N + 1):
    for c in range(1, N + 1):
      up_value, up_elements = dist[r - 1][c]
      left_value, left_elements = dist[r][c - 1]
      cost, element = matrix[r][c], elements[r][c]

      dist[r][c] = max(
        (up_value + cost, up_elements + element),
        (left_value + cost, left_elements + element)
      )

  return dist[N][N]

if __name__ == '__main__':
  N = int(input())
  matrix = [[0] * (N + 1) for _ in range(N + 1)]

  for r in range(N):
    data = [*map(int, input().split())]

    for c in range(N):
      matrix[r + 1][c + 1] = data[c]

  P = int(input())
  elements = [[0] * (N + 1) for _ in range(N + 1)]

  for _ in range(P):
    R, C = map(int, input().split())
    elements[R][C] += 1

  print(*solve(N, matrix, elements))
