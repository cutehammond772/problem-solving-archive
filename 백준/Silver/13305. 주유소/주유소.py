import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 10 ** 9 + 1

def solve(N, V, E):
  result, current = 0, INF

  for x in range(N - 1):
    current = min(current, V[x])
    result += current * E[x]

  return result

if __name__ == '__main__':
  N = int(input())
  E = [*map(int, input().split())]
  V = [*map(int, input().split())]

  print(solve(N, V, E))
