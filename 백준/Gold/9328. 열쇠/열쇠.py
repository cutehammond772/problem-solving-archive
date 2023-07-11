import sys
from queue import deque
input = lambda: sys.stdin.readline().rstrip()

PATH, WALL, DOC = 0, 1, 2
DEF_SYMBOLS = { '*': WALL, '.': PATH, '$': DOC }

# UP, DOWN, LEFT, RIGHT
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def convert(ch):
  if ch in DEF_SYMBOLS:
    return DEF_SYMBOLS[ch]

  # 알파벳을 ASCII 값으로 저장한다.
  return ord(ch)

def key_to_door(x):
  return ord(chr(x).upper())

def door_to_key(x):
  return ord(chr(x).lower())

def is_key(x):
  return ord('a') <= x <= ord('z')

def is_door(x):
  return ord('A') <= x <= ord('Z')

def entrances(N, M, matrix):
  result = []
  
  # row entrances
  for x in range(M):
    if matrix[0][x] != WALL:
      result.append((0, x))

    if matrix[N - 1][x] != WALL:
      result.append((N - 1, x))

  # column entrances
  for y in range(1, N - 1):
    if matrix[y][0] != WALL:
      result.append((y, 0))

    if matrix[y][M - 1] != WALL:
      result.append((y, M - 1))

  return result

def solve(N, M, matrix, initial_keys):
  result = 0
  
  visited = [[False] * M for _ in range(N)]
  routes = deque(entrances(N, M, matrix))

  # 지금까지 수집한 열쇠이다.
  keys = set(initial_keys)

  # 탐색 과정에서 맞닥뜨린 문의 정보를 나타낸다.
  resume = { x: [] for x in range(ord('A'), ord('Z') + 1) }
  
  while routes:
    row, col = routes.popleft()
    
    # 방문 관련
    if visited[row][col]:
      continue

    visited[row][col] = True
    element = matrix[row][col]
    
    # 문서일 경우
    if element == DOC:
      result += 1

    # 열쇠를 찾았을 경우
    if is_key(element) and element not in keys:
      to_resume = resume[key_to_door(element)]
      routes.extend(to_resume)
      to_resume.clear()
      
      keys.add(element)

    # 문을 맞닥뜨렸을 경우
    if is_door(element) and door_to_key(element) not in keys:
      visited[row][col] = False
      resume[element].append((row, col))
      continue

    # 다음 탐색 위치 선정
    for dir in directions:
      nrow, ncol = row + dir[0], col + dir[1]

      # 경계 체크
      if not (0 <= nrow < N and 0 <= ncol < M):
        continue

      if matrix[nrow][ncol] == WALL or visited[nrow][ncol]:
        continue

      routes.append((nrow, ncol))
      
  return result

if __name__ == '__main__':
  T = int(input())
  
  for _ in range(T):
    N, M = map(int, input().split())
    matrix = []
    
    for _ in range(N):
      matrix.append([convert(ch) for ch in input()])

    keys = input()

    if keys == '0':
      keys = set()
    else:
      keys = { convert(x) for x in keys }
      
    print(solve(N, M, matrix, keys))