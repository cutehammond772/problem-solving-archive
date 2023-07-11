import sys
input = lambda: sys.stdin.readline().rstrip()

INF = 11
PATH, WALL, HOLE = 0, 1, 2

DIRECTIONS = [(0, -1), (0, 1), (1, 0), (-1, 0)]
DONE, SAME, RED_GOAL, BLUE_GOAL = 0, 1, 2, 3

def load_board(N, M):
  board = [[INF] * M for _ in range(N)]
  RED, BLUE = (INF, INF) , (INF, INF)
  
  for row in range(N):
    # 보드 문자열 정보이다.
    raw = input()

    for col in range(M):
      ch = raw[col]

      # 해당 위치가 벽일 경우
      if ch == '#':
        board[row][col] = WALL
      # 해당 위치가 구멍인 경우  
      elif ch == 'O':
        board[row][col] = HOLE
      else:
        # 빨간 구슬의 위치인 경우
        if ch == 'R':
          RED = (row, col)
          
        # 파란 구슬의 위치인 경우
        if ch == 'B':
          BLUE = (row, col)

        board[row][col] = PATH
        
  return RED, BLUE, board

def solve(N, M, INIT_RED, INIT_BLUE, board):
  result = INF

  def move(RED, BLUE, DIR):
    rx, ry = RED
    bx, by = BLUE
    dx, dy = DIR
    
    status = DONE
    
    while True:
      nrx, nry, nbx, nby = rx, ry, bx, by

      if status != RED_GOAL:
        if board[rx + dx][ry + dy] != WALL:
          if board[rx + dx][ry + dy] == HOLE:
            status = RED_GOAL

          if (rx + dx, ry + dy) != (nbx, nby):
            nrx, nry = rx + dx, ry + dy
        
      if board[bx + dx][by + dy] != WALL:
        if board[bx + dx][by + dy] == HOLE:
          status = BLUE_GOAL
          break
          
        if (bx + dx, by + dy) != (nrx, nry):
          nbx, nby = bx + dx, by + dy

      if (nrx, nry) == (rx, ry) and (nbx, nby) == (bx, by):
        break

      rx, ry, bx, by = nrx, nry, nbx, nby

    # 처음과 같은 경우
    if RED == (rx, ry) and BLUE == (bx, by) and status == DONE:
      status = SAME
      
    return (rx, ry), (bx, by), status
  
  def recursion(RED, BLUE, count):
    nonlocal result
    
    if count >= result:
      return

    for DIR in DIRECTIONS:
      NEXT_RED, NEXT_BLUE, status = move(RED, BLUE, DIR)
      
      if status == SAME or status == BLUE_GOAL:
        continue

      if status == RED_GOAL:
        result = min(result, count + 1)
        break

      if status == DONE:
        recursion(NEXT_RED, NEXT_BLUE, count + 1)

  recursion(INIT_RED, INIT_BLUE, 0)
  return result

if __name__ == '__main__':
  # 보드의 세로, 가로 크기를 받는다.
  N, M = map(int, input().split())
  
  # RED, BLUE 위치는 별도로 둔다.
  RED, BLUE, board = load_board(N, M)

  # 백트래킹을 이용하여 최소값을 도출한다.
  result = solve(N, M, RED, BLUE, board)
  print(result if result <= 10 else -1)