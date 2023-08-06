import sys
input = lambda: sys.stdin.readline().rstrip()

def check(S, T):
  result = False

  if len(S) >= len(T):
    return S == T

  if T[0] == 'B':
    result = result or check(S, T[1:][::-1])

  if T[-1] == 'A':
    result = result or check(S, T[:-1])

  return result

if __name__ == '__main__':
  S, T = input(), input()
  print(1 if check(S, T) else 0)
