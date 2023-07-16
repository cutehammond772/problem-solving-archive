import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(W):
  result = 0

  for x in range(1, len(W) - 1):
    result = max(result, solve(W[:x] + W[(x + 1):]) + W[x - 1] * W[x + 1])

  return result

if __name__ == '__main__':
  N = int(input())
  W = [*map(int, input().split())]

  print(solve(W))
