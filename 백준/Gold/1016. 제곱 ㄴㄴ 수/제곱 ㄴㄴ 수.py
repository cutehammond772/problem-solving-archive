import sys
from math import floor, sqrt, ceil
input = lambda: sys.stdin.readline().rstrip()

def get_divisors(M):
  X, Y = 2, floor(sqrt(M)) + 1
  memo = [True] * Y
  
  for p in range(2, floor(sqrt(Y - 1)) + 1):
    if not memo[p]:
      continue

    for q in range(p * 2, Y, p):
      memo[q] = False
      
  return [x for x in range(X, Y) if memo[x]]

# K = P^2 * Q
def solve(N, M):
  result = M - N + 1
  memo = [False] * (M - N + 1)
  
  divisors = get_divisors(M)
  
  for X in divisors:
    divisor = X ** 2
    offset = ceil(N / divisor) * divisor
    
    for K in range(offset, M + 1, divisor):
      if memo[K - N]:
        continue
        
      memo[K - N] = True
      result -= 1
    
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  print(solve(N, M))