import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

# "리스트 문자열 입력"을 리스트로 변환
def parse(S):
  if S == '[]':
    return deque([])

  return deque([*map(int, S[1:-1].split(','))])

def solve(P, Q):
  reverse = False

  for cmd in P:
    if cmd == 'R':
      reverse = not reverse

    if cmd == 'D':
      if not Q:
        return "error"

      if reverse: Q.pop()
      else: Q.popleft()

  # 출력을 위한 전처리 과정
  Q = [*map(str, Q)]
  if reverse: Q.reverse()

  return f"[{','.join(Q)}]"

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    P, N, Q = input(), int(input()), parse(input())
    print(solve(P, Q))
