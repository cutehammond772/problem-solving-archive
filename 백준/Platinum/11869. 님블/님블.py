import sys, functools
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  input()
  P = [*map(int, input().split())]
  result = functools.reduce(lambda x, y: x ^ y, P)

  print("koosaga" if result else "cubelover")
