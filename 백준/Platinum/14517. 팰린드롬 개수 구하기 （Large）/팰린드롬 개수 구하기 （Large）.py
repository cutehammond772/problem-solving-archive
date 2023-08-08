import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10007

if __name__ == '__main__':
  L = len(S := input())

  # 인덱스 x부터 존재하는 팰린드롬 개수
  memo = [0] * L

  for x in range(L):
    memo[x] += (accu := 1)

    for y in range(x - 1, -1, -1):
      if S[x] == S[y]:
        accu = memo[y + 1] + 1

      memo[y] = (memo[y] + accu) % MOD

  print(memo[0])
