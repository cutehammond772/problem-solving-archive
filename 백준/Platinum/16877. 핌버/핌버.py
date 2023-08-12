import sys, functools
input = lambda: sys.stdin.readline().rstrip()
MAX = 3 * (10 ** 6)

def create(N):
  memo = [1, 1]

  while memo[-1] <= N:
    memo.append(memo[-1] + memo[-2])

  return memo

def solve(N, P):
  # 피보나치 수
  F = create(MAX)

  # 그런디 숫자(함수)
  G = [0] * (MAX + 1)

  for x in range(1, MAX + 1):
    candidates = set()

    for k in F:
      if x < k:
        break

      candidates.add(G[x - k])

    for i in range(max(candidates) + 2):
      if i not in candidates:
        G[x] = i
        break

  result = 0
  for x in range(N):
    result ^= G[P[x]]

  return result

if __name__ == '__main__':
  N = int(input())
  P = [*map(int, input().split())]

  result = solve(N, P)
  print("koosaga" if result else "cubelover")
