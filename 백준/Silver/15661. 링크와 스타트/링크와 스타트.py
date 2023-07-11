import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, matrix):
  result = 2 ** 63 - 1

  all = {x for x in range(N)}
  team = set()

  def calculate():
    diff = 0
    opposite = all - team

    for member in team:
      for partner in team:
        diff += matrix[member][partner]

    for member in opposite:
      for partner in opposite:
        diff -= matrix[member][partner]

    return abs(diff)

  def recursion(idx):
    nonlocal result

    if len(team) * (N - len(team)) > 0:
      diff = calculate()
      result = min(result, diff)

    for x in range(idx, N):
      team.add(x)
      recursion(x + 1)
      team.remove(x)

  recursion(0)
  return result

if __name__ == '__main__':
  N = int(input())
  matrix = [[*map(int, input().split())] for _ in range(N)]

  print(solve(N, matrix))