import sys
input = lambda: sys.stdin.readline().rstrip()

scores = [
  [10, 8, 7, 5, 1],
  [8, 6, 4, 3, 1],
  [7, 4, 3, 2, 1],
  [5, 3, 2, 2, 1],
  [1, 1, 1, 1, 0]
]

convert = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}

def solve(N, M, matrix):
  memo = [[-1] * (1 << M) for _ in range(N * M)]

  def get(x, y):
    rx, cx = x // M, x % M
    ry, cy = y // M, y % M

    return scores[matrix[rx][cx]][matrix[ry][cy]]

  def calculate(offset, bit):
    if offset >= N * M:
      return 0

    if memo[offset][bit] >= 0:
      return memo[offset][bit]

    result = 0

    # 1. 현 위치에 점유한 공간이 없는 경우
    if not bit & 1:
      # 1-1. 가로 두 칸을 점유할 경우
      if (offset + 1) % M and not bit & 2:
        result = max(result, get(offset, offset + 1) + calculate(offset + 2, bit >> 2))

      # 1-2. 세로 두 칸을 점유할 경우
      if (offset + M) < N * M:
        result = max(result, get(offset, offset + M) + calculate(offset + 1, (bit | 1 << M) >> 1))

    # 2. 해당 칸을 그냥 넘기는 경우
    result = max(result, calculate(offset + 1, bit >> 1))

    # 메모이제이션
    memo[offset][bit] = result
    return result

  return calculate(0, 0)

if __name__ == "__main__":
  N, M = map(int, input().split())
  matrix = [[convert[ch] for ch in input()] for _ in range(N)]

  print(solve(N, M, matrix))
