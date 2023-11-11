import sys
input = lambda: sys.stdin.readline().rstrip()

def gcd(A, B):
  if A < B:
    A, B = B, A

  while B:
    A, B = B, A % B

  return A

if __name__ == '__main__':
  A, B = map(int, input().split())
  Z = gcd(A, B)

  print(A * B // Z)
