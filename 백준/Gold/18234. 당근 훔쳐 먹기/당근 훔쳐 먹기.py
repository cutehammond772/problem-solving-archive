import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, T, carrots):
  # 1. 당근이 한 개이면, 마지막 날까지 최대한 기다렸다가 먹는 것이 이득이다.
  # - wi = pi이면, 심을 때마다 뽑아 먹든 기다리든 차이가 없지만,
  # - wi < pi이면, 최대한 기다렸다 먹는 것이 누적 맛의 최대가 된다.
  if N == 1:
    pi, wi = carrots[0]
    return wi + pi * (T - 1)

  # 2. 당근이 두 개 이상이면,
  # - 당근을 먹음으로써 생기는 누적 맛의 Loss를 최소화하도록 해야 한다.
  # - (T - (N - 1))일까지 기다린 다음, 증가폭이 작은 순서대로 먹어 치운다.
  # - wi <= pi이므로, 다시 심은 당근을 먹는 일은 없다.
  result = 0
  carrots.sort()

  for i in range(N):
    pi, wi = carrots[i]
    result += wi + pi * (T - (N - i))

  return result

if __name__ == '__main__':
  N, T = map(int, input().split())
  carrots = []

  for i in range(N):
    wi, pi = map(int, input().split())
    carrots.append((pi, wi))

  print(solve(N, T, carrots))