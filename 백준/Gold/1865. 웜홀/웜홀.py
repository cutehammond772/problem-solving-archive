import sys
input = lambda: sys.stdin.readline().rstrip()
UNDEFINED = 10000 * 499 + 1

def solve(dist, N):
  for k in range(N):
    for i in range(N):
      for j in range(N):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        if i == j and dist[i][j] < 0:
          return True
          
  return False

if __name__ == '__main__':
  TC = int(input())
  
  for _ in range(TC):
    N, M, W = map(int, input().split())
    result = False
    
    dist = [[UNDEFINED] * N for _ in range(N)]
    
    # 제자리는 0으로 초기화
    for x in range(N):
      dist[x][x] = 0
      
    # 도로 입력
    for _ in range(M):
      S, E, T = map(int, input().split())
      
      # 최소 길이의 도로만 취급
      dist[S - 1][E - 1] = dist[E - 1][S - 1] = min(dist[E - 1][S - 1], T)
  
    # 워프 입력
    for _ in range(W):
      S, E, T = map(int, input().split())
      dist[S - 1][E - 1] = min(dist[S - 1][E - 1], -T)
  
    # 체크
    check = solve(dist, N)
    print("YES" if check else "NO")