import sys
input = lambda: sys.stdin.readline().rstrip()
MAX = 1000000

def cards_mask(S):
  result = 0

  for num in S:
    result |= 1 << num

  return result

def mask(N):
  result = 0

  while N:
    result |= 1 << (N % 10)
    N //= 10

  return result

def primes():
  result = [True] * (MAX + 1)

  for x in range(2, int(MAX ** 0.5) + 1):
    if not result[x]:
      continue

    for y in range(x * 2, MAX + 1, x):
      result[y] = False

  return result

prime = primes()

def analyzer(S):
  nums = cards_mask(S)
  memo = [MAX] * (MAX + 1)

  def query(X):
    if memo[X] != MAX:
      return memo[X]

    if (mask(X) | nums) == nums:
      memo[X] = 0
      return 0

    if prime[X]:
      return MAX

    for Y in range(2, int(X ** 0.5) + 1):
      if X % Y:
        continue

      P, Q = query(Y), query(X // Y)

      if not (P == MAX or Q == MAX):
        memo[X] = min(memo[X], P + Q + 1)

    return memo[X]

  return query

if __name__ == '__main__':
  T = int(input())
  
  for _ in range(T):
    _, *S = map(int, input().split())
    query = analyzer(S)

    Q = int(input())

    for _ in range(Q):
      K = int(input())
      result = query(K)

      print(result if result != MAX else -1)
