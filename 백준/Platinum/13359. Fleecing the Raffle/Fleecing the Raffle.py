import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, P):
  X = 1
  result = P / (N + 1)
  
  while True:
    Y = X + 1
    next = (Y / X) / ((N + Y) / (N + Y - P))
    
    if next < 1.0:
      break
    
    result *= next
    X = Y
  
  return result

if __name__ == '__main__':
  N, P = map(int, input().split())
  print(solve(N, P))
  