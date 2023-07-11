import sys
input = lambda: sys.stdin.readline().rstrip()

COMMON_ORDER = [(1, 0), (0, -1), (0, 1), (-1, 0)]
ODD_ORDER = [(-1, 0), (1, 0), (0, -1)]

def solve(N, M):
  check = [[False] * M for _ in range(N)]
  stack = []

  for x in range(N):
    stack.append((x, 0))
    check[x][0] = True
    
  for y in range(1, M):
    stack.append((N - 1, y))
    check[N - 1][y] = True

  while stack[-1] != (0, 1):
    x, y = stack[-1]
      
    order = COMMON_ORDER
    
    if N % 2 == 1 and x < 2:
      order = ODD_ORDER
      
    for dx, dy in order:
      nx, ny = x + dx, y + dy
      
      if not (0 <= nx < N and 0 <= ny < M):
        continue

      if check[nx][ny]:
        continue
      
      stack.append((nx, ny))
      check[nx][ny] = True
      break
      
  return stack

if __name__ == '__main__':
  N, M = map(int, input().split())
  result = solve(N, M)
  
  print(len(result))
  for x, y in result:
    print(x + 1, y + 1)