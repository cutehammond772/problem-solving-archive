import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(x, y):
  if x < y:
    x, y = y, x

  while y:
    x, y = y, x % y

  return x

def lcm(bit, K, A):
  result = 1

  for i in range(K):
    if not (bit & (1 << i)):
      continue

    if result == 1:
      result = A[i]
    else:
      result = (result * A[i]) // gcd(result, A[i])

  return result

def count(x):
  result = 0

  while x:
    result += x & 1
    x >>= 1

  return result

# 포함-배제 원리 이용
def solve(N, K, A):
  result = 0

  for bit in range(1, 1 << K):
    sign = (-1) ** ((count(bit) + 1) % 2)
    result += sign * (N // lcm(bit, K, A))

  return result

if __name__ == "__main__":
  N, M = map(int, input().split())
  A = [*map(int, input().split())]

  print(solve(M, N, A))
