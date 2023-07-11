import sys
input = lambda: sys.stdin.readline().rstrip()

NaN = 2 ** 63 - 1

def solve(N, M):
  ALL_VISITED = 2 ** N - 1
  result = NaN
  
  # (bits for visit check, cost, node)
  stack = [(1, 0, 0)]
  memo = [[NaN] * N for _ in range(2 ** N)]
  
  while stack:
    visited, cost, node = stack.pop()
      
    for x in range(1, N):
      check = 1 << x
      dist = M[node][x]
      
      # 방문 여부 & 가능 경로 여부
      if dist == 0 or check & visited > 0:
        continue

      # 중간까지의 경로가 최종 경로 이상일 때
      if cost + dist >= result:
        continue
        
      next = visited | check

      # 중간 경로(끝이 X)의 최단거리 비교
      if memo[next][x] <= cost + dist:
        continue
        
      memo[next][x] = cost + dist
      
      # 다음 경로에서 모두 순회한 경우
      if next == ALL_VISITED:
        if M[x][0] != 0:
          result = min(result, cost + dist + M[x][0])
        continue
      
      stack.append((next, cost + dist, x))
      
  return result
    
if __name__ == '__main__':
  N = int(input())
  M = [list(map(int, input().split())) for _ in range(N)]
  
  print(solve(N, M))