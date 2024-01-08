import sys
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()

def solve(N, U):
  U.sort()

  # a + b = d - c로 나누어서 푼다.
  # d - c의 경우, d의 최대를 찾아야 하므로 dict로 둔다.
  adds, subs = set(), defaultdict(int)

  for i in range(N):
    for j in range(i, N):
      # 두 수의 합
      adds.add(U[i] + U[j])

      # 두 수의 차
      subs[U[j] - U[i]] = max(subs[U[j] - U[i]], U[j])

  result = 0

  for num in adds:
    if num in subs:
      result = max(result, subs[num])

  return result

if __name__ == '__main__':
  N = int(input())
  U = [int(input()) for _ in range(N)]

  print(solve(N, U))
