import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())

  count = 0
  memo = [[] for _ in range(N)]
  memo[0] = [1, 2]

  for x in range(1, N):
    for k in memo[x - 1]:
      memo[x] += [k * 10, k * 10 + 1, k * 10 + 2]

  for num in memo[N - 1]:
    if not num % 3:
      count += 1

  print(count)
