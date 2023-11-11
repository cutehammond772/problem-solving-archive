import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  queue = deque([(x + 1, A[x]) for x in range(N)])
  result, offset = [], 0

  # "3" 2 1 -3 -1
  # "-3" -1 2 1

  while queue:
    while offset:
      if offset > 0:
        queue.append(queue.popleft())
        offset -= 1
        continue

      if offset < 0:
        queue.appendleft(queue.pop())
        offset += 1
        continue

    number, move = queue.popleft()
    result.append(number)
    offset = move if move < 0 else move - 1

  print(*result)
