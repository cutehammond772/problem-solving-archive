import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

INF = -(10 ** 9 + 1)

def solve(N, D, Q):
  memo = [INF] * N
  heap = []
  
  for current in range(N):
    while heap:
      value, previous = heappop(heap)
      
      if current - previous > D:
        continue
      
      memo[current] = -value
      
      # 다시 넣는다.
      heappush(heap, (value, previous))
      break
    
    memo[current] = max(memo[current] + Q[current], Q[current])
    heappush(heap, (-memo[current], current))
    
  return max(memo)

if __name__ == '__main__':
  N, D = map(int, input().split())
  sequence = [*map(int, input().split())]
  
  print(solve(N, D, sequence))
  