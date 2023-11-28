import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  result, current = 1, 1

  for height in A:
    result = max(result, current := min(current, height))
    current += 1

  print(result)
