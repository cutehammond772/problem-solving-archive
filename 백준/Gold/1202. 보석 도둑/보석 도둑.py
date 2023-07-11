import sys
from heapq import heappop, heappush, heapify
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N, K = map(int, input().split())

  J = [tuple(map(int, input().split())) for _ in range(N)]
  heapify(J)
  
  B = sorted([int(input()) for _ in range(K)])

  result = 0
  heap = []
  
  for bag in B:
    while J and J[0][0] <= bag:
      M, V = heappop(J)
      heappush(heap, (-V, M))

    if heap:
      result += -heappop(heap)[0]
  
  print(result)
