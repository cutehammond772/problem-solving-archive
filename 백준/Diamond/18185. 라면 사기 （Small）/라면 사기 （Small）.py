import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, Q):
  result = 0

  for x in range(N):
    if x < N - 2:
      if Q[x + 1] > Q[x + 2]:
        # 앞의 2연속을 먼저 처리
        t = min(Q[x], Q[x + 1] - Q[x + 2])
        Q[x] -= t
        Q[x + 1] -= t
        result += 5 * t

        # 3연속을 이후에 처리
        t = min(Q[x], Q[x + 1], Q[x + 2])
        Q[x] -= t
        Q[x + 1] -= t
        Q[x + 2] -= t
        result += 7 * t
      else:
        # 3연속을 먼저 처리
        t = min(Q[x], Q[x + 1], Q[x + 2])
        Q[x] -= t
        Q[x + 1] -= t
        Q[x + 2] -= t
        result += 7 * t

        # 2연속을 이후에 처리
        t = min(Q[x], Q[x + 1])
        Q[x] -= t
        Q[x + 1] -= t
        result += 5 * t
    elif x < N - 1:
      # 2연속만 처리
      t = min(Q[x], Q[x + 1])
      Q[x] -= t
      Q[x + 1] -= t
      result += 5 * t

    # 마지막으로 현재 남은 라면 처리
    result += 3 * Q[x]

  return result

if __name__ == '__main__':
  N = int(input())
  sequence = [*map(int, input().split())]

  print(solve(N, sequence))
