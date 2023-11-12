import sys
input = lambda: sys.stdin.readline().rstrip()
OFF = 15000

def solve(N, M, A, B):
  memo = [False] * 30001
  memo[OFF] = True

  for x in range(1, N + 1):
    # 무게추를 구슬 쪽에 놓는 경우
    for i in range(A[x], 30001):
      memo[i - A[x]] |= memo[i]

    # 무게추를 추가하는 경우
    for i in range(30000 - A[x], -1, -1):
      memo[i + A[x]] |= memo[i]

  result = []

  for x in range(M):
    marble = B[x]

    # 최대 15000g까지만 잴 수 있다.
    if marble > 15000:
      result.append('N')
      continue

    result.append('Y' if memo[marble + OFF] else 'N')

  return result

if __name__ == '__main__':
  N = int(input())
  A = [0, *map(int, input().split())]

  M = int(input())
  B = [*map(int, input().split())]

  result = solve(N, M, A, B)
  print(*result)
