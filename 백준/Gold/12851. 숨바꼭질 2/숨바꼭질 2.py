import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
NaN = 100001

def measurer():
  temp, streak = NaN, 1
  
  def measure(time):
    nonlocal temp, streak
    if time < temp:
      temp, streak = time, 1
    elif time == temp:
      streak += 1
      
  def result():
    return streak
    
  return measure, result

def solve(N, K):
  # N이 더 큰 경우 뒤로만 가는 방법이 최선이다.
  if N >= K:
    return N - K, 1

  memo = [NaN] * 100001
  measure, result = measurer()
  queue = deque()

  memo[N] = 0
  queue.append((N, 0))
    
  while queue:
    X, time = queue.popleft()
    next = time + 1

    # Queue에서 꺼낸 시점에서 다시 확인
    if memo[X] < time:
      continue
      
    if X - 1 >= 0:
      if X - 1 == K:
        memo[K] = min(memo[K], next)
        measure(next)
      elif memo[X - 1] >= next:
        memo[X - 1] = next
        
        if memo[K] > next:
          queue.append((X - 1, next))

    if X + 1 <= 100000:
      if X + 1 == K:
        memo[K] = min(memo[K], next)
        measure(next)
      elif memo[X + 1] >= next:
        memo[X + 1] = next
        
        if memo[K] > next:
          queue.append((X + 1, next))

    if X * 2 <= 100000:
      if X * 2 >= K:
        calc = next + (X * 2) - K
        memo[K] = min(memo[K], calc)
        measure(calc)
      elif memo[X * 2] >= next:
        memo[X * 2] = next
        
        if memo[K] > next:
          queue.append((X * 2, next))

  return memo[K], result()


if __name__ == '__main__':
  N, K = map(int, input().split())
  time, solution = solve(N, K)

  print(time)
  print(solution)
