import sys, math
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  degrees = [0] * (N + 1)

  for _ in range(N - 1):
    P, Q = map(int, input().split())
    degrees[P] += 1
    degrees[Q] += 1

  leaves = degrees.count(1)
  print(math.ceil(leaves / 2))