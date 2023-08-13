import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = [*range(1, int(input()) + 1)]
  total = sum(N)

  print(total)
  print(total ** 2)
  print(sum(x ** 3 for x in N))
