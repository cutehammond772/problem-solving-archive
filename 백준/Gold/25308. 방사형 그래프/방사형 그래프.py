import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(A):
  mark = [False] * 8
  graph = []

  # 경우의 수
  result = 0

  # 볼록성 판정 (CCW 활용)
  def check():
    valid = True

    for i in range(8):
      a, b, c = graph[i - 1], graph[i], graph[(i + 1) % 8]

      if (a * c) - (b * (a + c)) / (2 ** 0.5) > 0:
        valid = False
        break

    return valid

  def find():
    nonlocal result

    if len(graph) == 8:
      result += check()
      return

    for i in range(8):
      if not mark[i]:
        mark[i] = True
        graph.append(A[i])
        find()
        mark[i] = False
        graph.pop()

  find()
  return result

if __name__ == "__main__":
  A = [*map(int, input().split())]
  print(solve(A))
