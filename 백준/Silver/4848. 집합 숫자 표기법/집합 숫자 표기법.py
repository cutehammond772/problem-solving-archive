import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  T = int(input())
  memo, mapper = [''] * (15 + 1), {}

  for x in range(15 + 1):
    memo[x] = f"{{{ ','.join(memo[:x]) }}}"
    mapper[memo[x]] = x

  for _ in range(T):
    P, Q = mapper[input()], mapper[input()]
    print(memo[P + Q])
