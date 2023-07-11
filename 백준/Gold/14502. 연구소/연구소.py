import sys
from queue import Queue

input = lambda: sys.stdin.readline().rstrip()
BLANK, WALL, VIRUS = 0, 1, 2

# 상 하 좌 우
dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def combination(matrix, N, M, fn):
  result = []

  def recursion(offset=0):
    nonlocal result

    if len(result) == 3:
      fn(tuple(result))
      return

    for x in range(offset, N * M):
      if matrix[x // M][x % M] != BLANK:
        continue

      result.append(x)
      recursion(x + 1)
      result.pop()

  recursion()

def area(matrix, N, M, walls, viruses, blanks):
  p, q, r = walls
  visit = set()
  blank_discount = 0

  que = Queue()

  for v in viruses:
    que.put(v)
    visit.add(v)
  
  while not que.empty():
    x = que.get()

    for i in range(4):
      nrow = x // M + dr[i]
      ncol = x % M + dc[i]
      next = nrow * M + ncol

      if not ((0 <= nrow < N) and (0 <= ncol < M)):
        continue

      if next == p or next == q or next == r:
        continue

      if next not in blanks or next in visit:
        continue

      blank_discount += 1
      que.put(next)
      visit.add(next)

  return len(blanks) - blank_discount - 3


def solve(matrix, N, M):
  viruses = set(i for i in range(N * M) if matrix[i // M][i % M] == VIRUS)
  blanks = set(i for i in range(N * M) if matrix[i // M][i % M] == BLANK)

  # 조합을 통해 벽의 조합을 생성한다. 이때 빈 공간만 걸러낸다.
  walls = []
  combination(matrix, N, M, walls.append)

  # 최대값을 반환한다.
  return max(area(matrix, N, M, w, viruses, blanks) for w in walls)

if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [list(map(int, input().split())) for _ in range(N)]

  result = solve(matrix, N, M)
  print(result)
