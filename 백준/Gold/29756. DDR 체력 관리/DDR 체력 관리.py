import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, S, H):
  memo = [-1] * 101
  
  # 처음 시작 때는 체력 100에 0점이다.
  memo[100] = 0
  
  for i in range(N):
    # 구간에 진입하기 전 체력 회복
    for x in range(100, -1, -1):
      memo[min(100, x + K)] = max(memo[min(100, x + K)], memo[x])
    
    # 구간을 플레이하는 경우
    for x in range(H[i], 101):
      memo[x - H[i]] = max(memo[x - H[i]], memo[x] + S[i])
  
  return max(memo)

if __name__ == "__main__":
  N, K = map(int, input().split())
  
  S = [*map(int, input().split())]
  H = [*map(int, input().split())]
  
  print(solve(N, K, S, H))
  