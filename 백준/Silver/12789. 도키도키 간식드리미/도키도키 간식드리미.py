import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  queue, wait = deque([*map(int, input().split())]), deque([])
  next = 1

  while queue or wait:
    # Case 1. 두 열에 학생이 모두 존재할 때
    if queue and wait:
      p, q = queue[0], wait[0]

      if next == p:
        queue.popleft()
        next += 1

      elif next == q:
        wait.popleft()
        next += 1

      else:
        wait.appendleft(queue.popleft())

    # Case 2. 기존 열에만 학생이 존재할 때
    elif queue and not wait:
      p = queue.popleft()

      if next == p:
        next += 1

      else:
        wait.appendleft(p)

    # Case 3. 새 1열에만 학생이 존재할 때
    elif not queue and wait:
      q = wait.popleft()

      if next == q:
        next += 1

      else:
        break

  print("Nice" if next > N else "Sad")
