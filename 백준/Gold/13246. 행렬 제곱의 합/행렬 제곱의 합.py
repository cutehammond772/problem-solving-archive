import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 1000

def resolve_bits(B):
  result = []

  while B:
    result.append(1 if B & 1 else 0)
    B >>= 1

  return result

def empty_matrix(N):
  return [[0] * N for _ in range(N)]

def unit_matrix(N):
  return [[1 if row == col else 0 for col in range(N)] for row in range(N)]

def multiply(N, m1, m2):
  result = empty_matrix(N)

  for row in range(N):
    for col in range(N):
      for num in range(N):
        result[row][col] = (result[row][col] + m1[row][num] * m2[num][col]) % MOD

  return result

def add(N, m1, m2):
  result = empty_matrix(N)

  for row in range(N):
    for col in range(N):
      result[row][col] = (m1[row][col] + m2[row][col]) % MOD

  return result

# (1) A + ... + A^(2^N) = A(A + 1)(A^2 + 1)...(A^(2^(N - 1)) + 1)
# (2) A^(2N + 1) + ... + A^(2N + N) = (A^(2N))(A + ... + A^N)
def solve(N, B, matrix):
  mult, total = [matrix], [matrix]
  bits = resolve_bits(B)
  unit = unit_matrix(N)

  for x in range(1, len(bits)):
    total.append(multiply(N, total[-1], add(N, mult[-1], unit)))
    mult.append(multiply(N, mult[-1], mult[-1]))

  result = empty_matrix(N)
  multiplier = unit

  for x in range(len(bits) - 1, -1, -1):
    if bits[x]:
      result = add(N, result, multiply(N, multiplier, total[x]))
      multiplier = multiply(N, multiplier, mult[x])

  return result

if __name__ == '__main__':
  N, B = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  result = solve(N, B, matrix)
  for row in result:
    print(*row)
