import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K):
  # [1, 2, 3, ..., N, N - 1, N - 2, ..., 3, 2, 1]

  # Case 1. 대각선 한 줄당 1초에 처리할 수 있는 경우
  if N <= K:
    return 2 * N - 1

  # Case 2. K가 1이면 병렬 처리가 불가능하다.
  if K == 1:
    return N * N

  # Case 2. 중간에 (처리 가능한 작업) > (컴퓨터 수)가 되는 경우
  # [1 to K] -> [(K + 1) to N to K] -> [K - 1, K - 2, K - 3, 1, 1]
  a = (K + 1 + N) * (N - K) // 2
  b = (K + N) * (N - K + 1) // 2

  result = (2 * K) + (a + b - N - 1) // K
  return result

if __name__ == "__main__":
  N, K = map(int, input().split())
  print(solve(N, K))
