import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N, M = map(int, input().split())
  S = {input() for _ in range(N)}

  result = 0
  for _ in range(M):
    if input() in S:
      result += 1

  print(result)
