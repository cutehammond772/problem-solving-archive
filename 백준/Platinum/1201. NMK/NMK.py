import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, K):

  # Case 1. M과 N의 합은 N + 1을 넘길 수 없다.
  if M + K > N + 1:
    return [-1]

  # Case 2. 한 쪽이 1인 경우 나머지는 N이어야 한다.
  if M == 1:
    if K != N:
      return [-1]

    return [*reversed(range(1, N + 1))]

  if K == 1:
    if M != N:
      return [-1]

    return [*range(1, N + 1)]

  # Case 3.
  X = (N - M) // (K - 1)

  if X > N:
    return [-1]

  # 기본 형태
  result = [*range(N - M + 1, N + 1)]
  temp = []

  for x in range(1, N - M + 1):
    temp.append(x)

    if len(temp) == K - 1:
      result += reversed(temp)
      temp = []

  result += reversed(temp)

  return result

if __name__ == '__main__':
  N, M, K = map(int, input().split())

  print(*solve(N, M, K))
