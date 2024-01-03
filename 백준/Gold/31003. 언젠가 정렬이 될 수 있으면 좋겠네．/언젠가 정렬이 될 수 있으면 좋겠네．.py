import sys
from heapq import heapify, heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

def gcd(x, y):
  if x > y:
    x, y = y, x

  while y:
    x, y = y, x % y

  return x

def solve(N, A):
  # dependency 그래프
  G = [[] for _ in range(N)]

  # 진입 차수
  degrees = [0] * N

  for node in range(N - 1):
    for next in range(node + 1, N):
      if gcd(A[node], A[next]) == 1:
        continue

      G[node].append(next)
      degrees[next] += 1

  # 가장 작은 수가 먼저 나오도록 함
  heap = [(A[node], node) for node in range(N) if degrees[node] == 0]
  heapify(heap)

  result = []

  while heap:
    element, node = heappop(heap)
    result.append(element)

    for next in G[node]:
      degrees[next] -= 1

      if degrees[next] == 0:
        heappush(heap, (A[next], next))

  return result

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  print(*solve(N, A))
