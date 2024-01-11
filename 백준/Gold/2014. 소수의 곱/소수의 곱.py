import sys
from heapq import heappush, heappop, heapify
input = lambda: sys.stdin.readline().rstrip()
MAX = 1 << 31

# 특정 수를 뽑을 때, 해당 수의 가장 큰 소인수부터 가장 작은 소인수까지 한 번씩 곱하여 힙에 추가한다.
def solve(K, N, A):
  heap = [(A[i], i) for i in range(K)]
  heapify(heap)

  result = 0

  duplicate = set(A)
  biggest = max(A)

  for t in range(N):
    num, last = heappop(heap)

    for i in range(last + 1):
      next = num * A[i]

      if next >= MAX:
        break

      if len(heap) + t >= 100000 and biggest < next:
        break

      if next not in duplicate:
        heappush(heap, (next, last))
        duplicate.add(next)

        biggest = max(biggest, next)

    result = num

  return result

if __name__ == '__main__':
  K, N = map(int, input().split())
  A = [*map(int, input().split())]

  print(solve(K, N, A))
