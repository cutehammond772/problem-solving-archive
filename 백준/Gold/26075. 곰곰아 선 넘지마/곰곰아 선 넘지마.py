import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, S, T):
  if N * M == 0:
    return 0

  # S와 T 내의 1을 왼쪽부터 하나씩 매칭시킨다. (-> 이동 횟수 최소)
  # 다른 1과는 상관없이 독립적으로 이동 횟수를 세면 된다.
  K, Z = 0, 0
  s_off, t_off = 0, 0

  # 총 이동 횟수가 홀수인 경우 1은 따로 Z에 저장한다.
  # 이렇게 되면 마지막까지 X, Y (=K)가 동일해지며, 이후 Z를 적절히 나누어 분배하면 된다.
  # 왜냐하면, Z는 X, Y 중 아무 곳에나 넣을 수 있으며, X와 Y가 최대한 균등해야 제곱의 합이 최소가 되기 때문이다.
  while s_off < len(S):
    if not S[s_off]:
      s_off += 1
      continue

    while not T[t_off]:
      t_off += 1

    dist = abs(s_off - t_off)
    K += dist // 2

    if dist % 2:
      Z += 1

    s_off += 1
    t_off += 1

  if Z % 2:
    return (K + Z // 2) ** 2 + (K + Z // 2 + 1) ** 2
  else:
    return 2 * ((K + Z // 2) ** 2)

if __name__ == '__main__':
  N, M = map(int, input().split())

  S = [int(ch) for ch in input()]
  T = [int(ch) for ch in input()]

  print(solve(N, M, S, T))
