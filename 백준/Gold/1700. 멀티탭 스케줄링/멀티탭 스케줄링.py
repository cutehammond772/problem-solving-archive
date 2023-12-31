import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, A):
  # 전기 용품의 사용 횟수가 플러그 수보다 같거나 작으면, 굳이 플러그를 뺄 필요가 없다.
  if N >= K:
    return 0

  # 각 전기 용품의 사용 순서를 나타낸다.
  orders = [deque([]) for _ in range(K + 1)]

  for i in range(K):
    orders[A[i]].append(i)

  # 현재 플러그 상태이다.
  occupied = []

  # 플러그를 뺀 횟수를 나타낸다.
  result = 0

  for i in range(K):
    appliance = A[i]

    # 이미 존재하는 경우
    if appliance in occupied:
      orders[appliance].popleft()
      continue

    # 빈 플러그가 존재하는 경우
    if len(occupied) < N:
      occupied.append(appliance)
      orders[appliance].popleft()
      continue

    # (등장 순서, 뺄 플러그의 위치)
    latest = (-1, -1)

    for k in range(N):
      if not orders[occupied[k]]:
        latest = max(latest, (101, k))

      else:
        latest = max(latest, (orders[occupied[k]][0], k))

    result += 1

    occupied[latest[1]] = appliance
    orders[appliance].popleft()

  return result

if __name__ == "__main__":
  N, K = map(int, input().split())
  A = [*map(int, input().split())]

  print(solve(N, K, A))
