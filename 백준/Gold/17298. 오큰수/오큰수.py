import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
  result = [-1] * N
  heap = []

  for x in range(N):
    value = A[x]

    while heap:
      if heap[0][0] >= value:
        break

      _, idx = heappop(heap)
      result[idx] = value

    heappush(heap, (value, x))

  return result

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  print(*solve(N, A))
