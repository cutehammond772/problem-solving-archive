import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  queue = deque([])

  for _ in range(N):
    P, *Q = map(int, input().split())

    if P == 1:
      queue.appendleft(Q[0])

    elif P == 2:
      queue.append(Q[0])

    elif P == 3:
      print(queue.popleft() if queue else -1)

    elif P == 4:
      print(queue.pop() if queue else -1)

    elif P == 5:
      print(len(queue))

    elif P == 6:
      print(1 if not queue else 0)

    elif P == 7:
      print(queue[0] if queue else -1)

    elif P == 8:
      print(queue[-1] if queue else -1)
