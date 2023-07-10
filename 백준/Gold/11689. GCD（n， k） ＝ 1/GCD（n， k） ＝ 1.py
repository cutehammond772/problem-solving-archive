import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
  result = 1
  MAX = int(N ** 0.5) + 1
  
  memo = [False] * MAX
  divisors = []
  
  for x in range(2, MAX):
    if memo[x] or N % x != 0:
      continue
      
    divisors.append(x)
    
    for y in range(x * 2, MAX, x):
      memo[y] = True
  
  for div in divisors:
    result *= (div - 1)
    
    while N % (div * div) == 0:
      N //= div
      result *= div
      
    N //= div
  
  if N > 1:
    result *= N - 1
    
  return result

if __name__ == '__main__':
  N = int(input())
  print(solve(N))
  