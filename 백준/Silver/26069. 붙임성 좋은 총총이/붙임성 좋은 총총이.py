import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  result = {'ChongChong'}

  for _ in range(N):
    A, B = input().split()

    if A in result or B in result:
      result.add(A)
      result.add(B)

  print(len(result))
