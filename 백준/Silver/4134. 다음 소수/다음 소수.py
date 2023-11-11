import sys
input = lambda: sys.stdin.readline().rstrip()

def check(x):
  for i in range(2, int(x ** 0.5) + 1):
    if x % i == 0:
      return False

  return True

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N = int(input())

    # 소수는 2부터 시작한다.
    if N <= 2:
      print(2)
      continue

    while not check(N):
      N += 1

    print(N)
