import math, sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

def pow(x, p):
  result = 1

  while p:
    result = (result * x) % MOD
    p -= 1

  return result

def phi(a):
  result = 1

  for x in range(2, math.ceil(math.sqrt(a)) + 1):
    count = 0

    while not a % x:
      count += 1
      a //= x

    if count:
      result = result * (x - 1) * pow(x, count - 1) % MOD

  if a > 1:
    result = result * (a - 1) % MOD

  return result

if __name__ == '__main__':
  T = int(input())

  # 성질: GCD 행렬의 행렬식은 집합의 모든 원소의 phi의 곱이다.
  # 참고: https://www.sciencedirect.com/science/article/pii/0024379592900429?via%3Dihub
  for _ in range(T):
    N = int(input())
    S = [*map(int, input().split())]

    result = 1
    for x in S:
      result = result * phi(x) % MOD

    print(result)
