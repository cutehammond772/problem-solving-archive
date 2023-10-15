import sys
input = lambda: sys.stdin.readline().rstrip()

# 제곱수의 끝자리 수는 [0, 1, 4, 5, 6, 9]만 가능하다.
valid = [1, 1, 0, 0, 1, 1, 1, 0, 0, 1]
d = [*range(9)]

def check(x):
  return int(x ** 0.5) ** 2 == x

def solve(N, M, matrix):
  result = -1
  stack = []

  # 끝자리 수부터 시작한다.
  for row in range(N):
    for col in range(M):
      num = matrix[row][col]

      if not valid[num]:
        continue

      if check(num):
        result = max(result, num)

      for r in range(9):
        for c in range(9):
          if r == c == 0:
            continue

          stack.append((row + d[r], col + d[c], d[r], d[c], num, 1))
          stack.append((row - d[r], col + d[c], -d[r], d[c], num, 1))
          stack.append((row + d[r], col - d[c], d[r], -d[c], num, 1))
          stack.append((row - d[r], col - d[c], -d[r], -d[c], num, 1))

  while stack:
    row, col, dr, dc, num, digit = stack.pop()

    if not (0 <= row < N and 0 <= col < M):
      continue

    num += (10 ** digit) * matrix[row][col]

    if check(num):
      result = max(result, num)

    stack.append((row + dr, col + dc, dr, dc, num, digit + 1))

  return result

if __name__ == "__main__":
  N, M = map(int, input().split())
  matrix = [[int(ch) for ch in input()] for _ in range(N)]

  print(solve(N, M, matrix))
