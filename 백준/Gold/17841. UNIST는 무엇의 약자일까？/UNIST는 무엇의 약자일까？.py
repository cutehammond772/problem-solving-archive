import sys
input = lambda: sys.stdin.readline().rstrip()
data = "UNIST"
MOD = int(1e9 + 7)

if __name__ == "__main__":
  N = int(input())
  result = 0

  # memo[i] = "UNIST"[..i]
  memo = [0] * 5

  for _ in range(N):
    W = input()
    offset = 0

    while offset < 5 and W[0] != data[offset]:
      end = offset = offset + 1

    if offset == 5:
      continue

    L = min(len(W), 5 - offset)

    for i in range(L):
      if W[i] != data[offset + i]:
        break

      # [0..i] + [i+1..j] = [0..j]
      memo[offset + i] += memo[offset - 1] if offset > 0 else 1
      memo[offset + i] %= MOD

  print(memo[4])
