import sys
from heapq import heapify, heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(heap):
  result = 0
  heapify(heap)

  while len(heap) > 1:
    P, Q = heappop(heap), heappop(heap)

    result += (P + Q)
    heappush(heap, P + Q)

  return result

if __name__ == '__main__':
  N = int(input())
  cards = [int(input()) for _ in range(N)]

  print(solve(cards))
