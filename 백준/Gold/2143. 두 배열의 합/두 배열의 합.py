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
      
def convert(X, A):
  result = []
  
  for x in range(X):
    result.append(A[x])
    
    for _ in range(x):
      result.append(result[-(1 + x)] + A[x])
      
  return result

if __name__ == '__main__':
  T = int(input())
  N, P = int(input()), list(map(int, input().split()))
  M, Q = int(input()), list(map(int, input().split()))

  count = 0
  
  # 부배열의 합을 구한 후 정렬한다.
  P = sorted(convert(N, P))
  Q = sorted(convert(M, Q))
  
  # Q의 한 조합(부배열의 합)에 대해 알맞는 P를 찾는다.
  for q in Q:
    target = T - q
    lower, upper = lower_bound(P, target), upper_bound(P, target)
    
    if lower >= len(P) or upper < 0:
      continue

    count += upper - lower + 1

  # 경우의 수를 출력한다.
  print(count)