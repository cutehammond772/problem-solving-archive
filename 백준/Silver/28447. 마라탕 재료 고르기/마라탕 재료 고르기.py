import sys
input = lambda: sys.stdin.readline().rstrip()

def comb(K, indexes, matrix):
  result = 0

  for x in range(K - 1):
    for y in range(x + 1, K):
      result += matrix[indexes[x]][indexes[y]]

  return result

def solve(N, K, matrix):
  result, current = -(2 ** 63 + 1), []

  def backtrack(offset):
    nonlocal result

    if len(current) == K:
      result = max(result, comb(K, current, matrix))
      return

    for x in range(offset, N):
      current.append(x)
      backtrack(x + 1)
      current.pop()

  backtrack(0)
  return result

if __name__ == '__main__':
  N, K = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  print(solve(N, K, matrix))
