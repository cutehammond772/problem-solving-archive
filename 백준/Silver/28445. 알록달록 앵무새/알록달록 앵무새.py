import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  DA, DB = input().split()
  MA, MB = input().split()

  total = [*set([DA, DB, MA, MB])]
  result = [(x, y) for x in total for y in total]
  result.sort()

  for p, q in result:
    print(p, q)
