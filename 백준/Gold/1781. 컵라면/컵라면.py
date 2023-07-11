import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(N, C, D):
  result = 0
  heap = []
  
  for idx in range(max(D), 0, -1):
    if idx in D:
      for cup in C[idx]:
        heappush(heap, cup)

    if heap:
      result += -heappop(heap)

  return result

def analyze(N):
  C = [[] for _ in range(200001)]
  D = set()
  
  for _ in range(N):
    dead, cup = map(int, input().split())
    
    C[dead].append(-cup)
    D.add(dead)
    
  return C, D

if __name__ == '__main__':
  N = int(input())
  C, D = analyze(N)

  print(solve(N, C, D))