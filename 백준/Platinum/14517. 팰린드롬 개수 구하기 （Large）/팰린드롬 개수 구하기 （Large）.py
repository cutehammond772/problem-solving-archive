import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10007

if __name__ == '__main__':
  S = input()
  L = len(S)

  # 인덱스 i부터 존재하는 팰린드롬 개수
  memo = [0] * L

  for x in range(L):
    accu = 1
    memo[x] += accu

    for y in range(x - 1, -1, -1):
      if S[x] == S[y]:
        accu = (memo[y + 1] + 1) % MOD

      memo[y] = (memo[y] + accu) % MOD

  print(memo[0])
