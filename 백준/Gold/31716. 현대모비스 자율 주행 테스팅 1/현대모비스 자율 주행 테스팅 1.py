import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e18)

def solve(N, K, track):
  # memo[row][col][start]
  memo = [[[INF, INF] for _ in range(N)] for _ in range(2)]
  
  # 초기 설정
  memo[0][0][0] = 0 if track[0][0] == '.' else INF
  memo[1][0][1] = 0 if track[1][0] == '.' else INF
  
  memo[0][0][1] = min(memo[0][0][1], memo[1][0][1] + 1) if track[0][0] == '.' else INF
  memo[1][0][0] = min(memo[1][0][0], memo[0][0][0] + 1) if track[1][0] == '.' else INF
  
  for start in range(2):
    for col in range(1, N):
      # 1. 직진
      for row in range(2):
        if track[row][col] == '#':
          continue
          
        memo[row][col][start] = min(memo[row][col][start], memo[row][col - 1][start] + 1)
      
      # 2. 차선 변경
      for row in range(2):
        if track[row][col] == '#':
          continue
          
        memo[row][col][start] = min(memo[row][col][start], memo[1 - row][col][start] + 1)
  
  result = INF
  
  if K == 1:
    result = min(result, memo[0][-1][0], memo[0][-1][1], memo[1][-1][0], memo[1][-1][1])
    return result if result < INF else -1
  
  if track[0][0] != '#' and track[0][-1] != '#':
    result = min(result, min(memo[0][-1][0], memo[0][-1][1]) + (memo[0][-1][0] * (K - 2)) + min(memo[0][-1][0], memo[1][-1][0]) + (K - 1))
  
  if track[1][0] != '#' and track[1][-1] != '#':
    result = min(result, min(memo[1][-1][0], memo[1][-1][1]) + (memo[1][-1][1] * (K - 2)) + min(memo[0][-1][1], memo[1][-1][1]) + (K - 1))
  
  return result if result < INF else -1

if __name__ == "__main__":
  N, K = map(int, input().split())
  track = [input() for _ in range(2)]
  
  print(solve(N, K, track))
  