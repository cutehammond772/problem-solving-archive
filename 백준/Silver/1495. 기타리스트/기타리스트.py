import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, S, M, V):
  memo = [[False] * (M + 1) for _ in range(N)]
  
  # 초기 설정
  if S - V[0] >= 0:
    memo[0][S - V[0]] = True
    
  if S + V[0] <= M:
    memo[0][S + V[0]] = True
    
  for x in range(1, N):
    for k in range(M + 1):
      if memo[x - 1][k]:
        if k - V[x] >= 0:
          memo[x][k - V[x]] = True
        
        if k + V[x] <= M:
          memo[x][k + V[x]] = True
  
  if True not in memo[-1]:
    return -1
  
  return max([x for x in range(M + 1) if memo[-1][x]])

if __name__ == '__main__':
  N, S, M = map(int, input().split())
  V = [*map(int, input().split())]
  
  print(solve(N, S, M, V))
  