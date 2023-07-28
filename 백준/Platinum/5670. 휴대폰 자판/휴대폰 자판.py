import sys
input = lambda: sys.stdin.readline().rstrip()
END = '.'

def make(S):
  root = {}

  for word in S:
    current = root

    for x in range(len(word)):
      ch = word[x]

      if ch not in current:
        current[ch] = {}

      current = current[ch]

    current[END] = {}

  return root

def solve(S):
  data = make(S)
  total = 0

  for word in S:
    current = data

    for x in range(len(word)):
      ch = word[x]

      if current == data or len(current) > 1:
        total += 1

      current = current[ch]

  return total / len(S)

if __name__ == '__main__':
  while N := input():
    N = int(N)
    S = [input() for _ in range(N)]

    print(f"{solve(S):.2f}")
