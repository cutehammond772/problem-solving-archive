import sys
input = lambda: sys.stdin.readline().rstrip()

def create(N):
  sequence = ['-'] * (3 ** N)
  queue = [(0, 3 ** N)]

  while queue:
    l, r = queue.pop()
    size = (r - l) // 3

    sequence[(l + size):(l + size * 2)] = [' '] * size

    if size > 1:
      queue.append((l, l + size))
      queue.append((l + 2 * size, r))

  return "".join(sequence)

if __name__ == '__main__':
  memo = [None] * 13

  while data := input():
    N = int(data)

    if not memo[N]:
      memo[N] = create(N)

    print(memo[N])
