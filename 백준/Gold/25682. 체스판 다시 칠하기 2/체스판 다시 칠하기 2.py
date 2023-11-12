import sys
input = lambda: sys.stdin.readline().rstrip()

B, W = 0, 1
convert = {'B': B, 'W': W}

def solve(N, M, K, matrix):
  # memo[p][q][r] : (p, q)칸까지 마지막 칸을 r(W or B)로 할 때 필요한 덧칠 수
  memo = [[[0, 0] for _ in range(M + 1)] for _ in range(N + 1)]

  # 1. 누적합을 위한 전처리
  for row in range(1, N + 1):
    for col in range(1, M + 1):
      # 해당 칸과 고정 칸이 다르면 새로 덧칠해야 한다.
      memo[row][col][W] = memo[row][col - 1][B] + (matrix[row][col] != W)
      memo[row][col][B] = memo[row][col - 1][W] + (matrix[row][col] != B)

    for col in range(1, M + 1):
      # 윗행의 값을 누적시킨다.
      memo[row][col][W] += memo[row - 1][col][B]
      memo[row][col][B] += memo[row - 1][col][W]

  # 2. 누적합을 이용하여 (K * K)칸의 최소 덧칠 수 구하기
  result = N * M

  for row in range(K, N + 1):
    for col in range(K, M + 1):
      for color in range(2):
        result = min(result,
                     memo[row][col][color]
                     - memo[row][col - K][(color + K) % 2]
                     - memo[row - K][col][(color + K) % 2]
                     + memo[row - K][col - K][color]
                     )

  return result

if __name__ == '__main__':
  N, M, K = map(int, input().split())
  matrix = [[-1] * (M + 1) for _ in range(N + 1)]

  for row in range(1, N + 1):
    data = input()

    for col in range(1, M + 1):
      matrix[row][col] = convert[data[col - 1]]

  print(solve(N, M, K, matrix))
