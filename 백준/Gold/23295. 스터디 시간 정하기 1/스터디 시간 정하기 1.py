import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N, T = map(int, input().split())

  available = [0] * 100002
  total = [0] * 100002

  for _ in range(N):
    K = int(input())

    for _ in range(K):
      x, y = map(int, input().split())

      available[x + 1] += 1
      available[y + 1] -= 1

  # imos trick
  for i in range(1, 100001):
    available[i] += available[i - 1]
    total[i] = total[i - 1] + available[i]

  result = (0, 0)

  for i in range(T, 100001):
    result = max(result, (total[i] - total[i - T], -(i - T)))

  print(-result[1], T - result[1])
