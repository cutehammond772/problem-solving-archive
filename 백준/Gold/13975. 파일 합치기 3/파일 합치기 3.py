import sys
from queue import deque
input = lambda: sys.stdin.readline().rstrip()

def pop(qs, qd):
  result = 0

  for _ in range(2):
    if len(qs) == 0:
      result += qd.popleft()
      continue
      
    if len(qd) == 0:
      result += qs.popleft()
      continue
      
    if qs[0] > qd[0]:
      result += qd.popleft()
    else:
      result += qs.popleft()
      
  return result

def solve(K, files):
  qs = deque(sorted(files))
  qd = deque()

  count = 0
  result = 0
  
  while count < K - 1:
    cost = pop(qs, qd)
    result += cost
    
    qd.append(cost)
    count += 1
    
  return result

if __name__ == '__main__':
  T = int(input())
  
  for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    
    print(solve(K, files))