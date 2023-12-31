import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, T, A):
  # 제일 적게 나도리가 담긴 바구니로부터 제일 많이 담긴 바구니로 옮긴다.
  A.sort()

  # 모두 0이면 모두 터진 것과 같다.
  if A.count(0) == N:
    return "YES"

  # x : 적은 쪽, y : 많은 쪽
  x, y = 0, N - 1

  while x < y:
    move = min(K - A[y], A[x])

    if move > T:
      return "NO"

    A[x], A[y], T = A[x] - move, A[y] + move, T - move

    if A[x] == 0:
      x += 1

    if A[y] == K:
      y -= 1

  # 한 바구니가 남는 경우, 해당 바구니는 아직 K개 미만으로 채워진 상태를 의미한다.
  if x == y:
    return "NO"

  return "YES"

if __name__ == "__main__":
  N, K, T = map(int, input().split())
  A = [*map(int, input().split())]

  print(solve(N, K, T, A))
