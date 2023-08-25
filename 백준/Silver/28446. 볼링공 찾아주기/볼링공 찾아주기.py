import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  M = int(input())
  A = {}

  for _ in range(M):
    P, *Q = map(int, input().split())

    if P == 1:
      X, W = Q
      A[W] = X

    if P == 2:
      W = Q[0]
      print(A[W])
