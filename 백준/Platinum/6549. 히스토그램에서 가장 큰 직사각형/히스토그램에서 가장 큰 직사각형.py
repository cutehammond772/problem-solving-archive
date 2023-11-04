import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":

  # Monotone Stack 이용
  while data := input():
    N, *B = map(int, data.split())

    if N == 0:
      break

    # (height, offset)
    stack = []
    result = 0

    for i in range(N):
      ch, co = B[i], i

      while stack:
        lh, lo = stack.pop()

        # 단조 증가를 유지한다.
        if lh < ch:
          stack.append((lh, lo))
          break

        co = min(co, lo)
        result = max(result, (i - lo) * lh)

      stack.append((ch, co))

    while stack:
      height, offset = stack.pop()
      result = max(result, (N - offset) * height)

    print(result)
