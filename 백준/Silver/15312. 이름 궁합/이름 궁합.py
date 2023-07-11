import sys
input = lambda: sys.stdin.readline().rstrip()
data = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

if __name__ == '__main__':
  memo = []
  P, Q = input(), input()

  for x in range(len(P) + len(Q)):
    if not x % 2:
      memo.append(data[ord(P[x // 2]) - ord('A')])
    else:
      memo.append(data[ord(Q[x // 2]) - ord('A')])

  for t in range(len(memo) - 1, 1, -1):
    for x in range(t):
      memo[x] = (memo[x] + memo[x + 1]) % 10

  print(f"{memo[0]}{memo[1]}")
