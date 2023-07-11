import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def solve(N, S):
  schedule = []
  S.sort()

  for x, y in S:
    if not schedule:
      heappush(schedule, y)
      continue

    min_endtime = schedule[0]
    
    if min_endtime <= x:
      # 기존 최소 종료 시간을 지운다.
      heappop(schedule)
      
    heappush(schedule, y)
    
  return len(schedule)

if __name__ == '__main__':
  N = int(input())
  S = [tuple(map(int, input().split())) for _ in range(N)]

  print(solve(N, S))