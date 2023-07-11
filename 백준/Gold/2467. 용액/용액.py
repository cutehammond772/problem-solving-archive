import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, k, off):
  x, y = off, len(A)
  
  while x < y:
    mid = (x + y) // 2
    
    if A[mid] >= k:
      y = mid
    else:
      x = mid + 1
      
  return x

def upper_bound(A, k, off):
  x, y = off, len(A)
  
  while x < y:
    mid = (x + y) // 2
    
    if A[mid] > k:
      y = mid
    else:
      x = mid + 1
    
  return x - 1

def solve(N, A):
  result = []
  diff = 2_000_000_001
  
  for x in range(N):
    target = -A[x]
    
    lower = lower_bound(A, target, x + 1)
    upper = upper_bound(A, target, x + 1)

    if lower < N:
      if diff > abs(A[x] + A[lower]):
        diff = abs(A[x] + A[lower])
        result = [A[x], A[lower]]

    if x < upper:
      if diff > abs(A[x] + A[upper]):
        diff = abs(A[x] + A[upper])
        result = [A[x], A[upper]]
        
  return sorted(result)

if __name__ == '__main__':
  N = int(input())
  A = list(map(int, input().split()))

  print(*solve(N, A))