import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
ADD, SORT, REV, STRAIGHT = 0, 1, 2, 3
EMPTY = (-1, None)

if __name__ == "__main__":
  N, Q, K = map(int, input().split())

  # (COMMAND, PARAMETER)
  tasks = [EMPTY] * Q

  # INDEX OF LATEST SORT COMMAND
  latest = -1

  for i in range(Q):
    C, *P = map(int, input().split())

    if C != SORT:
      tasks[i] = (C, P[0] if P else None)

    else:
      if latest >= 0:
        tasks[latest] = EMPTY

      latest = i
      tasks[latest] = (SORT, None)

  scheduler = deque([])
  mode = STRAIGHT

  for x in range(Q):
    C, P = tasks[x]

    if C < 0:
      continue

    if C == ADD:
      if mode == STRAIGHT:
        scheduler.append(P)

      else:
        scheduler.appendleft(P)

    # 모든 쿼리에서 한 번만 정렬이 일어난다.
    # REVERSE 또한 초기화된다.
    elif C == SORT:
      scheduler = deque(sorted(scheduler, reverse=True))
      mode = STRAIGHT

    elif C == REV:
      mode = REV if mode == STRAIGHT else STRAIGHT

  if mode == STRAIGHT:
    print(scheduler[-K])
  else:
    print(scheduler[K - 1])
