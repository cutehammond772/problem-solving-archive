import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(x, y):
  if x < y:
    x, y = y, x

  while y:
    x, y = y, x % y

  return x

def lcm(bit, K, C):
  result = 1

  for i in range(K):
    if not (bit & (1 << i)):
      continue

    if result == 1:
      result = C[i]
    else:
      result = (result * C[i]) // gcd(result, C[i])

  return result

def count(x):
  result = 0

  while x:
    result += x & 1
    x >>= 1

  return result

def solve(N, K, C):
  result = 0

  for bit in range(1, 1 << K):
    sign = (-1) ** ((count(bit) + 1) % 2)
    result += sign * (N // lcm(bit, K, C))

  return result

if __name__ == "__main__":
  N, L, R = map(int, input().split())
  C = [*map(int, input().split())]

  print(solve(R, N, C) - solve(L - 1, N, C))
