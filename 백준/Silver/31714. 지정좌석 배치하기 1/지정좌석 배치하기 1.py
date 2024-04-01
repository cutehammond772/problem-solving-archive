import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, D, T):
  for row in range(N):
    T[row].sort()
    
    if row == 0:
      continue
    
    for col in range(M):
      if T[row - 1][col] >= T[row][col] + D:
        return "NO"
  
  return "YES"

if __name__ == "__main__":
  N, M, D = map(int, input().split())
  T = [[*map(int, input().split())] for _ in range(N)]
  
  print(solve(N, M, D, T))
  