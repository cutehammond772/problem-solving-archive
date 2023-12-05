import sys
from math import sqrt
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()

# N까지의 소인수를 찾는다.
def primes(N):
  check = [True] * (N + 1)

  for num in range(2, int(sqrt(N)) + 1):
    if not check[num]:
      continue

    for next in range(num * 2, N + 1, num):
      check[next] = False

  return [num for num in range(2, N + 1) if check[num]]

def solve(N, A):
  # 1. 숫자가 하나이면 그대로 출력한다.
  if N == 1:
    return A[0], 0

  score, attempt = 1, 0

  # 소인수 2 ~ sqrt(10^6)
  P = primes(int(sqrt(1e6)))

  # 2-1. 모든 수에서 특정 소인수를 뽑아낸 다음 분배한다.
  for num in P:
    counts = [0] * N
    total = 0

    for i in range(N):
      count = 0

      while (A[i] % num) == 0:
        A[i] //= num
        count += 1

      counts[i] = count
      total += count

    # 분배가 가능한 경우
    if total >= N:
      multiplier = total // N
      score *= num ** multiplier

      # 시행 횟수 계산
      for i in range(N):
        diff = multiplier - counts[i]
        if diff > 0: attempt += diff

  # 2-2. 1000 이상의 소인수에 대해 처리한다.
  last_primes = defaultdict(int)

  for num in A:
    last_primes[num] += 1

  for prime in last_primes:
    if last_primes[prime] == N:
      score *= prime

  return score, attempt

if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]

  print(*solve(N, A))
