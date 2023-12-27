import sys
input = lambda: sys.stdin.readline().rstrip()

# 정방향 경로는 상근이가 M번 집으로 가는 과정에서 태우고 내려주면 된다.
# 역방향 경로의 경우, 최대한 겹치는 구간을 통합하여 이동 거리를 최소화한다.
def solve(M, A):
  total, end = 0, -1
  rev = []

  # 역방향 경로를 분류한다.
  for x, y in A:
    if x > y:
      rev.append((y, x))

  rev.sort()
  
  for x, y in rev:
    if end < x:
      total += y - x
      end = y

    total += max(0, y - end)
    end = max(end, y)

  # 왕복해야 하므로 각 구간의 두 배가 필요하다.
  return M + total * 2

if __name__ == "__main__":
  N, M = map(int, input().split())
  A = []

  for _ in range(N):
    x, y = map(int, input().split())
    A.append((x, y))

  print(solve(M, A))
