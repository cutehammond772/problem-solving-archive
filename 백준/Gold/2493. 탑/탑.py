import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
  N = int(input())
  Q = [*map(int, input().split())]

  result = [0] * N
  stack = []

  for x in range(N):
    top = (Q[x], x + 1)

    while stack and stack[-1][0] < top[0]:
      stack.pop()

    if not stack:
      stack.append(top)
      continue

    result[x] = stack[-1][1]
    stack.append(top)

  print(*result)
