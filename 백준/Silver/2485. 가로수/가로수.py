import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(A, B):
  if A < B:
    A, B = B, A

  while B:
    A, B = B, A % B

  return A

if __name__ == '__main__':
  N = int(input())
  A = [int(input()) for _ in range(N)]
  P, G = [], -1

  for i in range(N - 1):
    P.append(A[i + 1] - A[i])

    if G < 0:
      G = P[-1]

    else:
      G = gcd(G, P[-1])

  result = 0

  for i in range(len(P)):
    result += (P[i] // G) - 1

  print(result)
