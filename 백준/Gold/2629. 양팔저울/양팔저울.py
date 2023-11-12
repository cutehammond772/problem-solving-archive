import sys
input = lambda: sys.stdin.readline().rstrip()
OFF = 15000

def solve(N, M, A, B):
  memo = [[False] * 30001 for _ in range(N + 1)]
  memo[0][OFF] = True

  for x in range(1, N + 1):
    # 무게추를 사용하지 않는 경우
    for i in range(30001):
      memo[x][i] |= memo[x - 1][i]

    # 무게추를 구슬 쪽에 놓는 경우
    for i in range(A[x], 30001):
      memo[x][i - A[x]] |= memo[x - 1][i]

    # 무게추를 추가하는 경우
    for i in range(30001 - A[x]):
      memo[x][i + A[x]] |= memo[x - 1][i]

  result = []

  for x in range(M):
    marble = B[x]
    
    # 최대 15000g까지만 잴 수 있다.
    if marble > 15000:
      result.append('N')
      continue

    result.append('Y' if memo[N][marble + OFF] else 'N')

  return result

if __name__ == '__main__':
  N = int(input())
  A = [0, *map(int, input().split())]

  M = int(input())
  B = [*map(int, input().split())]

  result = solve(N, M, A, B)
  print(*result)
