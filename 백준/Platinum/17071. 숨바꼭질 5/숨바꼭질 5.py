import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

INF = 500001

def destinations(K):
  idx, time, addition = K, 0, 0
  result = {}
  
  while idx + addition < INF:
    result[idx + addition] = time
    
    idx += addition
    addition += 1
    time += 1

  return time, result

def solve(N, K):
  result = INF

  # 처음부터 N과 K가 같은 경우
  if N == K:
    return 0
  
  # 각 시간(0초 ~ N초에 대한 도착 지점)
  endtime, dest = destinations(K)

  # 홀수 위치, 짝수 위치에 대한 메모
  memo = [[INF] * 2 for _ in range(INF)]
  
  # BFS 처리를 위한 큐
  queue = deque([(N, 0)])
  
  while queue:
    x, time = queue.popleft()
    ntime = time + 1
    
    if ntime == endtime:
      break

    if ntime >= result:
      continue
    
    for y in ((x - 1), (x + 1), (x * 2)):
      if not 0 <= y < INF:
        continue
        
      # 첫 짝수 위치에 대해 처리
      if ntime % 2 == 0:
        if memo[y][0] < INF:
          continue
          
        memo[y][0] = ntime 
          
      # 첫 홀수 위치에 대해 처리
      if ntime % 2 > 0:
        if memo[y][1] < INF:
          continue
          
        memo[y][1] = ntime
        
      if (y in dest) and dest[y] >= ntime and (dest[y] - ntime) % 2 == 0:
        result = min(result, dest[y])
          
      queue.append((y, ntime))

  return result if result < INF else -1
    
if __name__ == '__main__':
  N, K = map(int, input().split())
  print(solve(N, K))