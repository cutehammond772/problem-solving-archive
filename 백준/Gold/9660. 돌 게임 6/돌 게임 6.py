import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  pattern = [1, 0, 1, 2, 3, 2, 0]

  if N == 0:
    print("CY")
  else:
    print("SK" if pattern[(N - 1) % 7] else "CY")
