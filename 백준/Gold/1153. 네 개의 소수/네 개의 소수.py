import sys
input = lambda: sys.stdin.readline().rstrip()

# 짝수인 경우: (짝수) + (짝수)로 나눈다.
# 홀수인 경우: (짝수) + (홀수)로 나누되, (홀수)의 경우 2 + (소수)로 표현되어야 한다.
def solve(N):
  # N이 8 미만인 경우 네 개의 소수로 나눌 수 없다.
  if N < 8:
    return [-1]

  # "짝수"를 두 개의 소수로 분해한다.
  def decompose(X):
    memo = [True] * (X + 1)

    for i in range(2, int(X ** 0.5) + 1):
      if not memo[i]:
        continue

      for j in range(i * 2, X + 1, i):
        memo[j] = False

    # 2 ~ X까지의 소수
    primes = [p for p in range(2, X + 1) if memo[p]]

    for p in primes:
      if memo[X - p]:
        return p, X - p

    return 0, 0

  # Case 1. N이 짝수인 경우
  if N % 2 == 0:
    # Case 1-1. N = (짝수) + (짝수)로 나타내어지는 경우
    if N % 4 == 0:
      a, b = decompose(N // 2)
      return [a, a, b, b]

    # Case 1-2. N = (홀수) + (홀수)로 나타내어지는 경우
    # -> (2 + 2) + (짝수)로 분해한다.
    else:
      a, b = decompose(N - 4)
      return [2, 2, a, b]

  # Case 2. N이 홀수인 경우
  # -> "짝수"는 항상 소수로 분해되므로 홀수는 적당히(2+3 = 5) 잡으면 된다.
  else:
    a, b = decompose(N - 5)
    return [2, 3, a, b]

if __name__ == "__main__":
  N = int(input())
  result = solve(N)

  result.sort()
  print(*result)
