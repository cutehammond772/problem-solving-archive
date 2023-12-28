import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(M, A):
  # 구간이 큰 것부터 나타나도록 정렬
  A.sort(key=lambda t: (t[0], -t[1]))

  available = 0
  end = 0
  count = 0

  for x, y in A:
    if end < x:
      count += end < available
      end = max(end, available)

    if end < x:
      break

    if end < y:
      available = max(available, y)

  if end < available:
    count += 1
    end = available

  if end < M:
    return 0

  return count

if __name__ == "__main__":
  while M := input():
    M = int(M)
    A = []

    while (data := input()) != "0 0":
      x, y = map(int, data.split())

      if y <= 0 or x >= M:
        continue

      A.append((max(0, x), min(y, M)))

    print(solve(M, A))
