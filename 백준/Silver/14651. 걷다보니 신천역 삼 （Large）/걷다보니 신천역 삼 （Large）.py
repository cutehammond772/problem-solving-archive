import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 9

if __name__ == '__main__':
  N = int(input())
  result = 2

  for x in range(N - 2):
    result = (result * 3) % MOD

  print(result if N != 1 else 0)
