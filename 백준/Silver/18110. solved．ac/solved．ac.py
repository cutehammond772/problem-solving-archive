import sys
input = lambda: sys.stdin.readline().rstrip()

def round(x):
  return int(x) + 1 if x - int(x) >= 0.5 else int(x)

def solve(N, S):
  if N == 0:
    return 0

  result = 0
  
  S.sort()
  cut = round(N * 0.15)
  
  for x in range(cut, N - cut):
    result += S[x]

  return round(result / (N - cut * 2))
  
if __name__ == '__main__':
  N = int(input())
  S = [int(input()) for _ in range(N)]

  print(solve(N, S))

  