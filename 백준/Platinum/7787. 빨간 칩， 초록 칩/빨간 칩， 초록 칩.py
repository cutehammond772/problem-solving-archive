import sys
input = lambda: sys.stdin.readline().rstrip()

# G(x)를 하나의 블록으로 생각하면,
# 1 * 1, 2 * 2, 4 * 4, 8 * 8, ..., (2 ^ n) * (2 ^ n) 크기의
# 블록으로 묶을 때 특유의 규칙이 존재한다.
def solve(A, B):
  ra, rb = A % 4, B % 4

  if ra == rb == 0:
    return solve(A >> 2, B >> 2)

  # 4n + 1, 2, 3번째 블록에서 1번째 블록과 3번째 블록의 대표값은 같다.
  if (ra, rb) in [(1, 1), (2, 2), (3, 3), (1, 3), (3, 1)]:
    return 'B'

  return 'A'

if __name__ == "__main__":
  A, B = map(int, input().split())
  winner = solve(A, B)

  print(f"{winner} player wins")
