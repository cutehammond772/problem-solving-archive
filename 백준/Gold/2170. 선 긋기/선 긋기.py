import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e9 + 1)

if __name__ == "__main__":
  N = int(input())
  A = []

  for _ in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

  result = 0
  end = -INF

  # 스위핑을 위해 (x, y) 순으로 정렬을 수행한다.
  A.sort()

  # 가장 왼쪽 선부터 훑어가며 선들의 길이를 구한다.
  for x, y in A:
    if end < x:
      result += y - x
      end = y

    result += max(0, y - end)
    end = max(end, y)

  print(result)
