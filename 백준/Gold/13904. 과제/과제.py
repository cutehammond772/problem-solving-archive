import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
  result = 0
  heap = []

  # 가장 나중인 마감일부터 고려한다.
  A.sort()

  # 마감일까지 남은 일수
  for day in range(1000, 0, -1):
    while A and A[-1][0] == day:
      heappush(heap, -A.pop()[1])

    if heap:
      result += -heappop(heap)

  return result

if __name__ == '__main__':
  N = int(input())
  A = []

  for _ in range(N):
    d, w = map(int, input().split())
    A.append((d, w))

  print(solve(A))
