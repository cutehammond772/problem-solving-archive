import sys
input = lambda: sys.stdin.readline().rstrip()

def preprocess(N):
  memo = [0] * (N + 1)

  for x in range(1, N + 1):
    for k in range(x, N + 1, x):
      memo[k] += x

    memo[x] += memo[x - 1]

  return memo

if __name__ == '__main__':
  T = int(input())
  memo = preprocess(10 ** 6)

  # 테스트 케이스
  for _ in range(T):
    print(memo[int(input())])