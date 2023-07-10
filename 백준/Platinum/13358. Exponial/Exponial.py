import sys
input = lambda: sys.stdin.readline().rstrip()

MEMO = [0, 1, 2, 9, 262144]

# 오일러 피 값 구하기
def phi(N):
  result = N
  
  for x in range(2, int(N ** 0.5) + 1):
    if N % x == 0:
      while N % x == 0:
        N = N // x
      
      result -= result / x
  
  if N > 1:
    result -= result / N
    
  return int(result)

# 분할 정복을 이용한 거듭 제곱 -> O(logN)
def pow(P, Q, M):
  result = 1
  
  while Q:
    if Q & 1:
      result = (result * P) % M
    
    P = (P * P) % M
    Q >>= 1
    
  return result

# 점화식
def calc(P, M):
  if P == 1 or M == 1:
    return 1
  
  result = pow(P, calc(P - 1, phi(M)), M)
  
  if P > 4 or MEMO[P] > M:
    result += M
  
  return result

def solve(N, M):
  if N == 1 or M == 1:
    return N % M
  
  return pow(N, calc(N - 1, phi(M)), M)

if __name__ == '__main__':
  N, M = map(int, input().split())
  print(solve(N, M))
  