import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(N, S, D):
  result = 0
  heap = []
  
  for idx in range(max(D), 0, -1):
    if idx in D:
      for pay in S[idx]:
        heappush(heap, pay)

    if heap:
      result += -heappop(heap)

  return result

def schedules(N):
  S = [[] for _ in range(10001)]
  D = { 0 }
  
  for _ in range(N):
    p, d = map(int, input().split())
    
    S[d].append(-p)
    D.add(d)
    
  return S, D

if __name__ == '__main__':
  N = int(input())
  S, D = schedules(N)

  print(solve(N, S, D))