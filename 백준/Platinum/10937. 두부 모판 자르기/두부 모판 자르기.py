import sys
input = lambda: sys.stdin.readline().rstrip()

scores = [
  [100, 70, 40, 0],
  [ 70, 50, 30, 0],
  [ 40, 30, 20, 0],
  [  0,  0,  0, 0]
]

convert = {'A': 0, 'B': 1, 'C': 2, 'F': 3}

def solve(N, matrix):
  memo = [[-1] * (1 << N) for _ in range(N * N)]

  def get(x, y):
    rx, cx = x // N, x % N
    ry, cy = y // N, y % N

    return scores[matrix[rx][cx]][matrix[ry][cy]]

  def calculate(offset, bit):
    if offset >= N * N:
      return 0

    if memo[offset][bit] >= 0:
      return memo[offset][bit]

    result = 0

    # 1. 현 위치에 점유한 공간이 없는 경우
    if not bit & 1:
      # 1-1. 가로 두 칸을 점유할 경우
      if (offset + 1) % N and not bit & 2:
        result = max(result, get(offset, offset + 1) + calculate(offset + 2, bit >> 2))

      # 1-2. 세로 두 칸을 점유할 경우
      if (offset + N) < N * N:
        result = max(result, get(offset, offset + N) + calculate(offset + 1, (bit | 1 << N) >> 1))

    # 2. 해당 칸을 그냥 넘기는 경우
    result = max(result, calculate(offset + 1, bit >> 1))

    # 메모이제이션
    memo[offset][bit] = result
    return result

  return calculate(0, 0)

if __name__ == "__main__":
  N = int(input())
  matrix = [[convert[ch] for ch in input()] for _ in range(N)]

  print(solve(N, matrix))
