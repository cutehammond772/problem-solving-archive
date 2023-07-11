import sys
input = lambda: sys.stdin.readline().rstrip()

UP, DOWN, LEFT, RIGHT = 0, 1, 2, 3
convert = { 'U': UP, 'D': DOWN, 'L': LEFT, 'R': RIGHT }
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def solve(N, M, matrix):
  memo = [-1] * (N * M)
  result = 0
  
  for k in range(N * M):
    if memo[k] != -1:
      continue

    # (root, pos)
    stack = [(k, k)]
    memo[k] = k
    
    while stack:
      root, node = stack.pop()
      nr, nc = (node // M) + dr[matrix[node]], (node % M) + dc[matrix[node]]
      next = nr * M + nc
      
      if not (0 <= nr < N and 0 <= nc < M):
        result += 1
        continue

      if memo[next] == root:
        result += 1
        continue

      if memo[next] != -1:
        continue
        
      memo[next] = root
      stack.append((root, next))
      
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  matrix = [0] * (N * M)
  
  for r in range(N):
    row = input()
    for c in range(M):
      matrix[r * M + c] = convert[row[c]]
      
  print(solve(N, M, matrix))