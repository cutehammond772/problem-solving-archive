import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
  result = []

  # a 오름차순 -> 길이가 긴 구간이 먼저 오도록 한다.
  A.sort(key=lambda t: (t[0], -t[1]))

  end = 0

  # (최대 구간, 가장 끝에 위치한 구간 이름)
  dist = (0, 0)

  for a, b, i in A:
    if end < min(a, dist[0]):
      result.append(dist[1])
      end = max(end, dist[0])

    if end < a:
      result.append(i)
      end = max(end, b)

    dist = max(dist, (b, i))

  if end < dist[0]:
    result.append(dist[1])

  # 구간 이름 순으로 정렬
  result.sort()
  return result

if __name__ == "__main__":
  N = int(input())
  A = []

  for i in range(1, N + 1):
    a, b = map(int, input().split())
    A.append((a, b, i))

  result = solve(A)

  print(len(result))
  print(*result)
