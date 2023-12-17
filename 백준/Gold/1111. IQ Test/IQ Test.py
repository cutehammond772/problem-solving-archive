import sys
input = lambda: sys.stdin.readline().rstrip()

# ax1 + b = x2
# ax2 + b = x3
# (1) a = (x2 - x3) / (x1 - x2), b = x2 - ax1 (if. x1 != x2)
# (2) a = 0 (if. x1 == x2)
def solve(N, Q):
  # Case 1. 숫자가 1개이면 점화식 판별이 불가능하다. (A)
  if N == 1:
    return "A"

  # Case 2-1. 숫자가 2개 주어질 때, 동일한 수가 아닐 경우 점화식 판별이 불가능하다. (A)
  if N == 2 and Q[0] != Q[1]:
    return "A"

  # Case 2-2. 숫자가 2개 주어질 때, 동일한 수가 주어질 경우 그 다음 수도 같은 수가 도출된다.
  if N == 2 and Q[0] == Q[1]:
    return Q[1]

  # Case 3-1. 숫자가 3개 이상 주어질 때, 점화식을 세울 수 있으므로 해당 점화식과 수가 일치하는지 비교한다.
  if Q[0] != Q[1]:
    p, q = Q[1] - Q[2], Q[0] - Q[1]

    # a = p / q 에서 a는 정수여야 한다.
    if p % q:
      return "B"

    # 점화식을 도출한 후 모든 수에 대해 체크한다.
    a = p // q
    b = Q[1] - a * Q[0]

    for i in range(N - 1):
      if (a * Q[i]) + b != Q[i + 1]:
        return "B"

    return a * Q[N - 1] + b

  # Case 3-2. x1 == x2인 경우 모든 수가 같지 않으면 점화식이 성립하지 않는다. (B)
  else:
    return Q[1] if len(set(Q)) == 1 else "B"

if __name__ == "__main__":
  N = int(input())
  Q = [*map(int, input().split())]

  print(solve(N, Q))
