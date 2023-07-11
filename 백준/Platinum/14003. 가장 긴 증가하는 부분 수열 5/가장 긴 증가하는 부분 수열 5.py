import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(arr, k):
  p, q = 0, len(arr) - 1
  
  while p != q:
    mid = (p + q) // 2
    if arr[mid] >= k:
      q = mid
    else:
      p = mid + 1
      
  return p

def solve(N, A):
  memo = []
  marker = []
  
  for i in range(N):
    if i == 0:
      memo.append(A[0])
      marker.append(0)
      continue

    if memo[-1] < A[i]:
      memo.append(A[i])
      marker.append(len(memo) - 1)
      continue
      
    idx = lower_bound(memo, A[i])
    memo[idx] = A[i]
    marker.append(idx)
      
  return memo, marker

def get_lcs(M, N, A, marker):
  offset = M - 1
  result = [-1] * M
  
  for x in range(N - 1, -1, -1):
    if offset < 0:
      break
      
    if marker[x] == offset:
      result[offset] = A[x]
      offset -= 1
      
  return result

if __name__ == '__main__':
  N = int(input())
  A = list(map(int, input().split()))
  memo, marker = solve(N, A)
  
  print(len(memo))
  print(*get_lcs(len(memo), N, A, marker))