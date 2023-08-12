import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  G = [0] * (N + 1)

  # 다각형을 선분을 기준으로 두 다각형으로 나눈다.
  for x in range(2, N + 1):
    candidates = set()

    for k in range(x - 1):
      candidates.add(G[k] ^ G[x - k - 2])

    for k in range(max(candidates) + 2):
      if k not in candidates:
        G[x] = k
        break

  print(1 if G[N] else 2)
