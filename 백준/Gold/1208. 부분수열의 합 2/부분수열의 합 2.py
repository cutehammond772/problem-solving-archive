import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
  x, y = 0, len(A)
  
  while x < y:
    mid = (x + y) // 2
    
    if A[mid] >= K:
      y = mid
    else:
      x = mid + 1
      
  return x

def upper_bound(A, K):
  x, y = 0, len(A)
  
  while x < y:
    mid = (x + y) // 2
    
    if A[mid] > K:
      y = mid
    else:
      x = mid + 1
      
  return x - 1

def subset_sums(A, K):
  result = [0]
  
  for x in range(K):
    for i in range(2 ** x):
      result.append(result[i] + A[x])
      
  return result[1:]

def solve(N, S, A):
  result = 0
  
  # A 배열을 그대로 사용하면 '2^40'가지의 경우의 수가 필요하므로, 나누어서 계산한다.
  P = sorted(subset_sums(A[:(N // 2)], N // 2))
  Q = sorted(subset_sums(A[(N // 2):], N - (N // 2)))
  
  # 먼저 각 배열마다의 존재 여부를 판단한다.
  result += P.count(S) + Q.count(S)
    
  # 두 배열 간의 조합으로 존재 여부를 판단한다.
  for x in range(len(Q)):
    target = S - Q[x]
    
    size = upper_bound(P, target) - lower_bound(P, target)
    
    if size >= 0:
      result += (size + 1)
      
  return result
  
if __name__ == '__main__':
  N, S = map(int, input().split())
  A = list(map(int, input().split()))

  print(solve(N, S, A))
