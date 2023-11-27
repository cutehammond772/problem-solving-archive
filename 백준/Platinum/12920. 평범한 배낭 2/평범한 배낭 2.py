import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N, M = map(int, input().split())
  things = []

  for _ in range(N):
    V, C, K = map(int, input().split())
    
    # 자연수 분할로 O(K) -> O(logK) 최적화
    while K > 1:
      things.append((V * (K // 2), C * (K // 2)))
      K -= K // 2

    things.append((V, C))

  memo = [-1] * (M + 1)
  memo[0] = 0

  for weight, value in things:
    for total in range(M, weight - 1, -1):
      if memo[total - weight] >= 0:
        memo[total] = max(memo[total], memo[total - weight] + value)

  print(max(memo))