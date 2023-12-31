import sys
input = lambda: sys.stdin.readline().rstrip()

# 표현 가능한 범위를 확장한다는 개념으로 생각해본다.
def solve(N, A):
  A.sort()
  right = 0

  for i in range(N):
    if right < A[i] - 1:
      return right + 1

    right += A[i]

  return right + 1

if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]

  print(solve(N, A))
