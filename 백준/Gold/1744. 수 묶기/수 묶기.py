import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, Q):
  result, offset = 0, 0

  while offset < N:
    if offset + 1 >= N:
      result += Q[offset]
      break

    x, y = Q[offset], Q[offset + 1]

    if x + y <= x * y:
      result += x * y
      offset += 2
      continue

    result += x
    offset += 1

  return result

if __name__ == '__main__':
  N = int(input())
  sequence = [int(input()) for _ in range(N)]
  P, Q = [x for x in sequence if x > 0], [x for x in sequence if x <= 0]

  P.sort(reverse=True)
  Q.sort()

  print(solve(len(P), P) + solve(len(Q), Q))
