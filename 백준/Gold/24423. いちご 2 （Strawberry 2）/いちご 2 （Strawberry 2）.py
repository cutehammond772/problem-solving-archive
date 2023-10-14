import sys
input = lambda: sys.stdin.readline().rstrip()

# 해당 딸기가 가운데에 위치함을 기준으로 한다.
dh, dw = [0, 0, 1, 1, 1, 0, -1, -1, -1], [0, 1, 1, 0, -1, -1, -1, 0, 1]

# 딸기 위치의 기준점을 변경시켜, 모든 경우의 3 * 3 구역을 판단할 수 있도록 한다.
oh, ow = [-1, -1, -1, 0, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def solve(S, C):
  result = 0

  def check(h, w):
    result = 0

    for i in range(9):
      count = 0

      for j in range(9):
        nh, nw = h + oh[i] + dh[j], w + ow[i] + dw[j]

        if (nh, nw) in S:
          count += C[(nh, nw)]

      result = max(result, count)

    return result

  for h, w in S:
    result = max(result, check(h, w))

  return result

if __name__ == "__main__":
  # 실질적으로 필요하지는 않다.
  H, W = map(int, input().split())
  N, S, C = int(input()), set(), dict()

  for _ in range(N):
    A, B = map(int, input().split())

    if (A, B) in S:
      C[(A, B)] += 1
    else:
      S.add((A, B))
      C[(A, B)] = 1

  print(solve(S, C))
