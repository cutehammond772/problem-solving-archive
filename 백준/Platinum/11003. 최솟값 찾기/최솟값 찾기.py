import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# Increasing Monotone Queue
def solve(N, L, A):
  result = []
  queue = deque([])

  idx = 0
  for offset in range(N):
    if queue and queue[0] < offset - (L - 1):
      queue.popleft()

    while idx < offset + 1:
      while queue and A[queue[-1]] >= A[idx]:
        queue.pop()

      queue.append(idx)
      idx += 1

    result.append(A[queue[0]])

  return result

if __name__ == '__main__':
  N, L = map(int, input().split())
  A = [*map(int, input().split())]

  print(*solve(N, L, A))
