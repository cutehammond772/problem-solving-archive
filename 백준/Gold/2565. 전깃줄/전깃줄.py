import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  order = []

  for _ in range(N):
    x, y = map(int, input().split())
    order.append((x, y))

  seq = [o[1] for o in sorted(order)]

  # seq의 LIS의 길이가 곧 전깃줄의 최대 매칭이다.
  L = len(seq)
  memo = [1] * L

  for x in range(L):
    for y in range(x):
      if seq[y] < seq[x]:
        memo[x] = max(memo[x], 1 + memo[y])

  print(L - max(memo))
