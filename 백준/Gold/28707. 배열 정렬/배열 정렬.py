import sys
from collections import deque, defaultdict

input = lambda: sys.stdin.readline().rstrip()
INF = int(1e18)

def analyse(A, E):
  result = defaultdict(lambda: INF)
  candidate = deque()
  
  result[tuple(A)] = 0
  candidate.append((0, tuple(A)))
  
  while candidate:
    cost, sequence = candidate.popleft()
    
    if result[sequence] < cost:
      continue
    
    for l, r, c in E:
      # swapping
      next_seq = [*sequence]
      next_seq[l], next_seq[r] = next_seq[r], next_seq[l]
      next_seq = tuple(next_seq)
      
      # check
      if result[next_seq] <= cost + c:
        continue
      
      result[next_seq] = cost + c
      candidate.append((cost + c, next_seq))
  
  return result
  
def solve(A, E):
  analysis = analyse([*sorted(A)], E)
  result = analysis[tuple(A)]
  
  return result if result < INF else -1

if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]
  
  M = int(input())
  E = []
  
  for _ in range(M):
    l, r, c = map(int, input().split())
    E.append((l - 1, r - 1, c))
  
  print(solve(A, E))
  