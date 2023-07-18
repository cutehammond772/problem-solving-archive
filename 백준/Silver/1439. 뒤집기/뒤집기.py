import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  S = [int(x) for x in input()]
  total = [0, 0]

  # first index
  total[S[0]] += 1

  for x in range(1, len(S)):
    if S[x - 1] != S[x]:
      total[S[x]] += 1

  print(min(total))
