import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  L = [int(input()) for _ in range(N)]
  result = 0

  # (키, 특정 위치)
  stack = [(L[0], -1)]
  
  for x in range(1, N):
    previous = 0

    while stack:
      last, same = stack.pop()

      if last < L[x]:
        if previous:
          result += 1

        previous = last
        continue

      stack.append((last, same))

      if previous:
        result += 1

      break

    # 동일한 키의 연속성 판단
    if stack and L[x] == stack[-1][0]:
      stack.append((L[x], stack[-1][1] + 1))
    else:
      if not stack:
        stack.append((L[x], -1))
      else:
        stack.append((L[x], 0))

    result += max(0, stack[-1][1])

  # (N - 1)은 인접한 두 키의 쌍을 나타냄
  print(result + (N - 1))
