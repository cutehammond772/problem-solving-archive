import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  while N := int(input()):
    sequence = [int(input()) for _ in range(N)]
    result = current = sequence[0]

    for x in range(1, N):
      current = max(sequence[x], current + sequence[x])
      result = max(result, current)

    print(result)
    