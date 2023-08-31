import sys
input = lambda: sys.stdin.readline().rstrip()
MAX, MOD = 300, (10 ** 9) + 7

def solve(S):
  L = len(S)

  # 문자열의 길이가 홀수이면 올바른 괄호 문자열이 성립될 수 없다.
  if L % 2:
    return 0

  # memo는 괄호로 덮인 문자열을 나타낸다. ex) memo[a][b] => (...)
  memo = [[0] * MAX for _ in range(MAX)]

  # result는 다양한 조합을 나타낸다. ex) result[a][b] = (..)(...)(..)
  result = [[0] * MAX for _ in range(MAX)]

  # 특정 길이의 괄호 문자열 C에 대해,
  for size in range(2, L + 1, 2):
    for off in range(L - (size - 1)):
      a, b = off, off + size - 1

      # Case 1. 특정 위치를 기준으로 (result) + (memo)로 나누어 생각한다.
      for x in range(2, size, 2):
        result[a][b] = (result[a][b] + (result[a][a + (x - 1)] * memo[a + x][b])) % MOD

      # Case 2. "C = (A)" 와 같이 괄호로 감싼다.
      if S[a] != S[b]:
        total = result[a + 1][b - 1]

        if size == 2:
          memo[a][b] = result[a][b] = 1
        else:
          result[a][b] = (result[a][b] + total) % MOD
          memo[a][b] = total

  return result[0][L - 1]

if __name__ == '__main__':
  S = input()
  print(solve(S))
