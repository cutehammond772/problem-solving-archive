import sys
input = lambda: sys.stdin.readline().rstrip()

# 뤼카 정리
def solve(N, K, M):
  memo = [[0] * 2001 for _ in range(2001)]
  result = 1
  
  # 파스칼의 삼각형을 통해 이항 계수 생성
  for n in range(M + 1):
    memo[n][0] = 1
    
    for r in range(1, n + 1):
      memo[n][r] = (memo[n - 1][r] + memo[n - 1][r - 1]) % M
  
  # M진법
  while N or K:
    result = (result * memo[N % M][K % M]) % M
    N, K = N // M, K // M
  
  return result
  
if __name__ == '__main__':
  N, K, M = map(int, input().split())
  print(solve(N, K, M))
