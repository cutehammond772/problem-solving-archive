import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, W, P):
  memo = [False] * 400001
  
  for x in range(N):
    for y in range(x + 1, N):
      T = W - (P[x] + P[y])
      
      if T <= 0 or T > 400000:
        continue
        
      if memo[T]:
        return "YES"
    
    for y in range(x):
      if P[x] + P[y] < W:
        memo[P[x] + P[y]] = True
  
  return "NO"

if __name__ == '__main__':
  W, N = map(int, input().split())
  P = [*map(int, input().split())]
  
  print(solve(N, W, P))
  
  
