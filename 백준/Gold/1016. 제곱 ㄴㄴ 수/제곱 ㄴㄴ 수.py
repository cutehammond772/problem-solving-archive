import sys
from math import floor, sqrt, ceil
input = lambda: sys.stdin.readline().rstrip()

# K = P^2 * Q
def solve(N, M):
  result = M - N + 1
  memo = set()
  
  for X in range(2, floor(sqrt(M)) + 1):
    divisor = X ** 2
    offset = ceil(N / divisor) * divisor
    
    for K in range(offset, M + 1, divisor):
      if K in memo:
        continue
        
      memo.add(K)
      result -= 1
    
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  print(solve(N, M))