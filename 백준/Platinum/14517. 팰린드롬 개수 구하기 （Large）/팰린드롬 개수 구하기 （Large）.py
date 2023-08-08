import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10007
off = ord('a')

if __name__ == '__main__':
  S = input()
  L = len(S)

  # 인덱스 i부터 존재하는 팰린드롬 개수
  memo = [0] * len(S)

  for x in range(L):
    char = ord(S[x]) - off
    accumulation = 1
    memo[x] += accumulation

    for y in range(x - 1, -1, -1):
      if ord(S[y]) - off == char:
        accumulation = (memo[y + 1] + 1) % MOD

      memo[y] = (memo[y] + accumulation) % MOD

  print(memo[0])
