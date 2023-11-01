import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, matrix):
  memo = [[-1] * (1 << M) for _ in range(N * M)]

  def calculate(offset, bit):
    if offset >= N * M:
      return 0

    if memo[offset][bit] >= 0:
      return memo[offset][bit]

    result = 0

    # '1' 블록 놓기
    if not bit & 1:
      result = max(result, 1 + calculate(offset + 1, (bit | (matrix[offset + M] << M)) >> 1))

    # '4' 블록 놓기
    if (offset + 1) % M and (offset + M) < N * M and not bit & 3:
      check = matrix[offset + M] | (matrix[offset + (M + 1)] << 1)

      if not check & 3:
        result = max(result, 16 + calculate(offset + 2, (bit | (3 << M)) >> 2))

    # 특정 블럭이 점유한 경우
    result = max(result, calculate(offset + 1, (bit | (matrix[offset + M] << M)) >> 1))

    # 메모이제이션
    memo[offset][bit] = result
    return result

  initial = 0

  for col in range(M):
    initial |= matrix[col] << col

  return calculate(0, initial)

if __name__ == "__main__":
  M, N = map(int, input().split())
  matrix = [0] * ((N + 1) * M)

  # 이미 놓여진 '1' 블록의 개수이다.
  count = 0

  for col in range(M):
    data = input()

    for row in range(N):
      matrix[row * M + col] = 1 if data[row] == '1' else 0
      count += matrix[row * M + col]

  print(count + solve(N, M, matrix))
