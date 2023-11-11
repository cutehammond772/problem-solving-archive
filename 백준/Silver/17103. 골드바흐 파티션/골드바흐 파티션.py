import sys
input = lambda: sys.stdin.readline().rstrip()

def preprocess(N):
  check = [True] * (N + 1)
  check[0] = check[1] = False

  for i in range(2, int(N ** 0.5) + 1):
    if not check[i]:
      continue

    for j in range(i * 2, N + 1, i):
      check[j] = False

  return check, [x for x in range(2, N + 1) if check[x]]

if __name__ == '__main__':
  T = int(input())
  check, primes = preprocess(10 ** 6)

  for _ in range(T):
    N = int(input())
    count = 0

    for prime in primes:
      if N // 2 < prime:
        break

      count += check[N - prime]

    print(count)
