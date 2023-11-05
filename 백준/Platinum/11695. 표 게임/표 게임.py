import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
  N, M = map(int, input().split())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  result = 0

  for row in range(N):
    result ^= sum(matrix[row])

  print("august14" if result else "ainta")
