import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
  result = []

  # 중간값을 기준으로 right가 left보다 1개 ~ 2개 더 많도록 유지한다.
  left, right = [], []

  for i in range(N):
    num = A[i]

    if right and right[0] >= num:
      heappush(left, -num)
    else:
      heappush(right, num)

    if len(right) - len(left) > 2:
      heappush(left, -heappop(right))

    if len(right) - len(left) < 1:
      heappush(right, -heappop(left))

    result.append(right[0])

  return result

if __name__ == '__main__':
  N = int(input())
  A = [int(input()) for _ in range(N)]

  result = solve(N, A)
  print(*result, sep='\n')
