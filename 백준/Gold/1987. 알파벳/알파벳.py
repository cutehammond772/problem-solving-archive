import sys
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]

def solve(R, C, M):
  stack = [(0, 0, M[0][0], 1)]
  result = 1
  
  while stack:
    r, c, visit, count = stack.pop()
    result = max(result, count)

    for i in range(4):
      nr, nc = r + dr[i], c + dc[i]
      
      if not (0 <= nr < R and 0 <= nc < C):
        continue

      if M[nr][nc] & visit > 0:
        continue
      
      stack.append((nr, nc, M[nr][nc] | visit, count + 1))
      
  return result

if __name__ == '__main__':
  R, C = map(int, input().split())
  M = [[0] * C for _ in range(R)]

  for r in range(R):
    row = input()
    for c in range(C):
      M[r][c] = 1 << (ord(row[c]) - ord('A'))
      
  print(solve(R, C, M))