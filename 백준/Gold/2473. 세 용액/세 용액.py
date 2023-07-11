import sys
from itertools import combinations

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
  diff = 3_000_000_001

  # 세 개 중 두 개는 조합으로 찾은 후 나머지 하나를 이분탐색으로 찾는다. 
  for x, y in combinations(range(N), 2):
    target = -(A[x] + A[y])
    
    lower = lower_bound(A, target, y + 1)
    upper = upper_bound(A, target, y + 1)

    if lower < N:
      if diff > abs(A[x] + A[y] + A[lower]):
        diff = abs(A[x] + A[y] + A[lower])
        result = [A[x], A[y], A[lower]]

    if y < upper:
      if diff > abs(A[x] + A[y] + A[upper]):
        diff = abs(A[x] + A[y] + A[upper])
        result = [A[x], A[y], A[upper]]
        
  return sorted(result)

if __name__ == '__main__':
  N = int(input())
  A = list(map(int, input().split()))
  A.sort()
  
  print(*solve(N, A))