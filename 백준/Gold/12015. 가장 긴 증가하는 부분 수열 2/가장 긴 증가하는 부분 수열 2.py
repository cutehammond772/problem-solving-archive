import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(memo, k):
  x, y = 0, len(memo) - 1
  
  while x != y:
    mid = (x + y) // 2
    
    if memo[mid] >= k:
      y = mid
    else:
      x = mid + 1
      
  return x

def solve(N, A):
  memo = []
  
  for x in range(N):
    if x == 0:
      memo.append(A[x])
      continue
      
    if memo[-1] < A[x]:
      memo.append(A[x])
    else:
      idx = lower_bound(memo, A[x])
      memo[idx] = A[x]
      
  return len(memo)

if __name__ =='__main__':
  N = int(input())
  A = list(map(int, input().split()))

  print(solve(N, A))