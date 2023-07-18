import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  S = input()
  substrings = set()

  for x in range(len(S)):
    for y in range(x, len(S)):
      substrings.add(S[x:(y + 1)])

  print(len(substrings))
