import sys
from heapq import heapify, heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
  heap = []

  max_Ak = 0
  result = 10 ** 9

  for i in range(N):
    max_Ak = max(max_Ak, A[i])
    heap.append(A[i])

  heapify(heap)

  while heap[0] * 2 <= max_Ak:
    Ak = heappop(heap)
    result = min(result, max_Ak - Ak)
    max_Ak = max(max_Ak, Ak * 2)

    heappush(heap, Ak * 2)

  # 추가적으로 N번 더 수행한다.
  for _ in range(N):
    Ak = heappop(heap)
    result = min(result, max_Ak - Ak)
    max_Ak = max(max_Ak, Ak * 2)

    heappush(heap, Ak * 2)

  return result

if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]

  print(solve(N, A))
