import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# Decreasing Monotone Queue
def solve(N, M, A):
  result = []

  L = 2 * M - 1
  queue = deque([])

  idx = 0
  for offset in range(N - L + 1):
    if queue and queue[0] < offset:
      queue.popleft()

    while idx < offset + L:
      while queue and A[queue[-1]] <= A[idx]:
        queue.pop()

      queue.append(idx)
      idx += 1

    result.append(A[queue[0]])

  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  A = [*map(int, input().split())]

  print(*solve(N, M, A))
