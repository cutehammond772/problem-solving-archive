import sys
input = lambda: sys.stdin.readline().rstrip()
MAX = 2 ** 63 - 1

def resolve(P, Q):
  return min(P[0] + Q[0], P[1] + Q[1])

# 10을 만드는 수는 2와 5 뿐이므로, 이 둘만 고려하면 된다.
# 각 위치에 대해, 2가 최소인 경우와 5가 최소인 경우를 각각 구한다.
def solve(N, K, S):
  if N - 1 <= K:
    return min(S[0][0] + S[-1][0], S[0][1] + S[-1][1])

  # (min_twos, min_fives)
  memo = []

  for x in range(N):
    twos, fives = S[x]

    if x == 0:
      memo.append([twos, fives])
    else:
      memo.append([MAX, MAX])

    for y in range(max(x - K, 0), x):
      m_twos, m_fives = memo[y]

      memo[x][0] = min(memo[x][0], m_twos + twos)
      memo[x][1] = min(memo[x][1], m_fives + fives)

  return min(memo[-1])

def convert(X):
  X = int(X)
  twos, fives = 0, 0

  while not X % 2:
    twos += 1
    X //= 2

  while not X % 5:
    fives += 1
    X //= 5

  return twos, fives

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N, K = map(int, input().split())
    S = [*map(convert, input().split())]

    print(solve(N, K, S))
