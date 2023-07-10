import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(lines, D):
  result = 0
  
  # 도착 지점을 기준으로 오름차순 정렬
  lines.sort(key=lambda t: t[1])
  heap = []
  
  for p, q in lines:
    heappush(heap, (p, q))
    
    while heap:
      p1, q1 = heap[0]
      
      if not (p1 >= q - D and q1 <= q):
        heappop(heap)
      else:
        break
    
    result = max(result, len(heap))
  
  return result
  
if __name__ == '__main__':
  N = int(input())
  lines = []
  
  for _ in range(N):
    P, Q = map(int, input().split())
    
    if P > Q:
      P, Q = Q, P
      
    lines.append((P, Q))
  
  D = int(input())

  print(solve(lines, D))
  