import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
MAX = 2 ** 63 - 1

def solve(S):
  result = MAX
  
  # memo[count][clip] = min_time
  memo = [[MAX] * 1000 for _ in range(2000)]
  
  # (count, clip, time)
  queue = deque([(1, 0, 0)])
  
  while queue:
    count, clip, time = queue.popleft()
    
    if time + 1 > result:
      continue
    
    # count가 S에 도달하지 않았을 때
    if count < S:
      if count != clip and memo[count][count] > time + 1:
        memo[count][count] = time + 1
        queue.append((count, count, time + 1))
      
      if clip > 0:
        next = count + clip
        
        if next == S:
          result = min(result, time + 1)
          
        if memo[next][clip] > time + 1:
          memo[next][clip] = time + 1
          queue.append((next, clip, time + 1))
        
    # 뒤로만 가기
    if count > 0:
      queue.append((count - 1, clip, time + 1))
  
  return min(memo[S])
  
if __name__ == '__main__':
  S = int(input())
  print(solve(S))
  