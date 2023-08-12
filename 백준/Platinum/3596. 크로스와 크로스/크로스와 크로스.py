import sys
input = lambda: sys.stdin.readline().rstrip()

def mex(nums):
  upper = max(nums) + 1

  for x in range(upper):
    if x not in nums:
      return x

  return upper

if __name__ == '__main__':
  N = int(input())

  # Grundy Numbers
  G = [0] * (N + 1)

  # G(0) = 0이다.
  for x in range(1, N + 1):
    candidates = set()

    for k in range(x):
      candidates.add(G[max(0, k - 2)] ^ G[max(0, x - k - 3)])

    G[x] = mex(candidates)

  print(1 if G[N] else 2)
