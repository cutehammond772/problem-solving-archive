import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, Q):
  memo = [[] for _ in range(20)]

  # 특정 1의 자리수의 존재 여부 확인
  for num in Q:
    for i in range(20):
      if num & (1 << i):
        memo[i].append(num)

  # 가장 높은 자리수부터 확인
  for x in range(19, -1, -1):
    if len(memo[x]) < K:
      continue

    result = 1 << x
    current = memo[x]

    for y in range(x - 1, -1, -1):
      next = [t for t in current if t & (1 << y)]

      if len(next) >= K:
        result |= 1 << y
        current = next

    return result

  return 0

if __name__ == "__main__":
  N, K = map(int, input().split())
  Q = map(int, input().split())

  print(solve(N, K, Q))
