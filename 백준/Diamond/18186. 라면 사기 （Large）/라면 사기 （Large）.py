import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, Q, X, Y, Z):
  result = 0

  for x in range(N):
    if x < N - 2:
      if Q[x + 1] > Q[x + 2]:
        # 앞의 2연속을 먼저 처리
        t = min(Q[x], Q[x + 1] - Q[x + 2])
        Q[x] -= t
        Q[x + 1] -= t
        result += Y * t

        # 3연속을 이후에 처리
        t = min(Q[x], Q[x + 1], Q[x + 2])
        Q[x] -= t
        Q[x + 1] -= t
        Q[x + 2] -= t
        result += Z * t
      else:
        # 3연속을 먼저 처리
        t = min(Q[x], Q[x + 1], Q[x + 2])
        Q[x] -= t
        Q[x + 1] -= t
        Q[x + 2] -= t
        result += Z * t

        # 2연속을 이후에 처리
        t = min(Q[x], Q[x + 1])
        Q[x] -= t
        Q[x + 1] -= t
        result += Y * t
    elif x < N - 1:
      # 2연속만 처리
      t = min(Q[x], Q[x + 1])
      Q[x] -= t
      Q[x + 1] -= t
      result += Y * t

    # 마지막으로 현재 남은 라면 처리
    result += X * Q[x]

  return result

if __name__ == '__main__':
  N, B, C = map(int, input().split())
  Q = [*map(int, input().split())]
  
  X, Y, Z = B, B + C, B + 2 * C
  
  if B < C:
    X, Y, Z = B, B * 2, B * 3
  
  print(solve(N, Q, X, Y, Z))
