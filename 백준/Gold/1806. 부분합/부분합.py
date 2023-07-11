import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, S, A):
  accumulation, result = 0, N + 1
  x1 = 0
  
  for x2 in range(N):
    accumulation += A[x2]
      
    while accumulation >= S:
      result = min(result, x2 - x1 + 1)
      
      accumulation -= A[x1]
      x1 += 1
      
  if result == N + 1:
    return 0
    
  return result

if __name__ == '__main__':
  N, S = map(int, input().split())
  A = list(map(int, input().split()))
  
  print(solve(N, S, A))