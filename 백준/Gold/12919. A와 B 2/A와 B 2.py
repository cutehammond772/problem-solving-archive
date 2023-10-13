import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(S, T):
  candidates = [T]

  while candidates:
    candidate = candidates.pop()

    if len(candidate) <= len(S):
      if candidate == S:
        return 1

      continue

    if candidate[-1] == 'A':
      candidates.append(candidate[:-1])

    if candidate[0] == 'B':
      candidates.append(candidate[1:][::-1])

  return 0

if __name__ == "__main__":
  S, T = input(), input()
  print(solve(S, T))
