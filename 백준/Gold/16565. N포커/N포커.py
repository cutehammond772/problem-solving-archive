import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10007

# 1Ck ~ 52Ck 조합 생성
def combinations(N):
  memo = [[0] * (N + 1) for _ in range(N + 1)]

  for n in range(1, N + 1):
    for r in range(N + 1):
      if r == 0 or n == r:
        memo[n][r] = 1
        continue

      memo[n][r] = (memo[n - 1][r] + memo[n - 1][r - 1]) % MOD

  return memo

# 0! ~ 13! 생성
def factorials(N):
  memo = [1]

  for x in range(1, N + 1):
    memo.append(memo[-1] * x)

  return memo

def pow(x, y):
  result = 1

  while y:
    if y & 1:
      result = (result * x) % MOD

    y >>= 1
    x = (x ** 2) % MOD

  return result

def solve(N):
  combs = combinations(52)
  facts = factorials(13)

  # Case 1. 4장 미만으로는 어떤 포카드도 만들 수 없다.
  if N < 4:
    return 0

  # Case 2. 비둘기집의 원리에 의해 최소 하나 이상의 포카드가 성립한다.
  if N > 39:
    return combs[52][N]

  # Case 3. (N개의 카드를 뽑는 경우의 수) - (포카드가 하나도 성립하지 않는 경우의 수)를 구한다.
  counts = [0] * 4
  total = 0

  def recursion(remain, off):
    nonlocal total

    if sum(counts) > 13:
      return

    if not remain:
      T = sum(counts)
      one, two, three = counts[1:]

      result = (combs[13][T] * (facts[T] // (facts[one] * facts[two] * facts[three]))) % MOD

      result = (result * pow(4, one)) % MOD
      result = (result * pow(6, two)) % MOD
      result = (result * pow(4, three)) % MOD

      total = (total + result) % MOD
      return

    for x in range(off, 3 + 1):
      counts[x] += 1
      recursion(remain - x, x)
      counts[x] -= 1

  recursion(N, 1)
  return (combs[52][N] - total) % MOD

if __name__ == '__main__':
  N = int(input())
  print(solve(N))
