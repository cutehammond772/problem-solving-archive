import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  memo = [0] * (N + 1)

  for x in range(1, N + 1):
    if x < 7:
      memo[x] = x
      continue

    memo[x] = max(memo[x - 3] * 2, memo[x - 4] * 3, memo[x - 5] * 4)

  # 성질 1. Ctrl+A, Ctrl+C, Ctrl+V는 한몸이다. 서로 떨어져 있을 때보다 같이 붙어있을 때 최대이기 때문이다.
  # 성질 2. Ctrl+V의 경우 연속으로 최대 3번까지 쓸 수 있다.
  # -> 4번 이상 사용할 경우 Ctrl+A,C,V를 두 번 사용하는 것이 이득이다. 왜냐하면, 값은 동일하게 4배로 증가하지만
  # 버퍼가 두 배 차이나기 때문이다.
  print(memo[N])
