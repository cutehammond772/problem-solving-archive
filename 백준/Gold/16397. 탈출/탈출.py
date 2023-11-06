import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def button_B(x):
  if x == 0:
    return 0

  x *= 2
  fragment = []

  while x:
    fragment.append(x % 10)
    x //= 10

  fragment[-1] -= 1
  result = 0

  while fragment:
    digit = fragment.pop()
    result = result * 10 + digit

  return result

def solve(N, T, G):
  memo = [T + 1] * 100000

  queue = deque([(N, 0)])
  memo[N] = 0

  if N == G:
    return memo[N]

  while queue:
    number, count = queue.popleft()
    next_count = count + 1

    # T회를 초과하여 버튼을 누르는 경우
    if next_count > T:
      continue

    # A 버튼을 누르는 경우
    num_A = number + 1

    if num_A < 100000 and memo[num_A] > next_count:
      memo[num_A] = next_count

      if num_A != G:
        queue.append((num_A, next_count))

    # B 버튼을 누르는 경우
    num_B = button_B(number)

    if number * 2 < 100000 and memo[num_B] > next_count:
      memo[num_B] = next_count

      if num_B != G:
        queue.append((num_B, next_count))

  return memo[G] if memo[G] < T + 1 else "ANG"

if __name__ == "__main__":
  N, T, G = map(int, input().split())
  print(solve(N, T, G))
