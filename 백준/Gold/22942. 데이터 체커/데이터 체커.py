import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
  # 같은 시작 지점일 때 선분의 길이가 더 큰 원부터 오도록 한다.
  A.sort(key=lambda t: (t[0], -t[1]))
  stack = []

  for p, q in A:
    while stack:
      np, nq = stack[-1]

      if np < p and q < nq:
        break

      if nq < p:
        stack.pop()

      else:
        return False

    stack.append((p, q))

  return True

if __name__ == '__main__':
  N = int(input())
  A = []

  for _ in range(N):
    x, r = map(int, input().split())

    # 원의 양 끝 두 점을 잇는 선분을 추가한다.
    A.append((x - r, x + r))

  print("YES" if solve(A) else "NO")
