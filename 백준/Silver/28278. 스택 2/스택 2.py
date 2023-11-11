import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  stack = []

  for _ in range(N):
    P, *Q = map(int, input().split())

    if P == 1:
      stack.append(Q[0])

    elif P == 2:
      print(stack.pop() if stack else -1)

    elif P == 3:
      print(len(stack))

    elif P == 4:
      print(1 if not stack else 0)

    elif P == 5:
      print(stack[-1] if stack else -1)
