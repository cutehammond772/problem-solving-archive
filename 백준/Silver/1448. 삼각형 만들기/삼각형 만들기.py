import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
  # 내림차순으로 정렬한다.
  A.sort(reverse=True)

  # A[x]는 삼각형 중 가장 큰 변에 해당된다.
  for x in range(N - 2):
    if A[x] < A[x + 1] + A[x + 2]:
      return A[x] + A[x + 1] + A[x + 2]

  return -1

if __name__ == '__main__':
  N = int(input())
  A = [int(input()) for _ in range(N)]

  print(solve(N, A))
