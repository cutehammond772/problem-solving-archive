import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A, B):
  ra, rb = A % 4, B % 4

  if ra == rb == 0:
    return solve(A >> 2, B >> 2)

  if (ra, rb) in [(1, 1), (2, 2), (3, 3), (1, 3), (3, 1)]:
    return 'B'

  return 'A'

if __name__ == "__main__":
  A, B = map(int, input().split())
  winner = solve(A, B)

  print(f"{winner} player wins")
