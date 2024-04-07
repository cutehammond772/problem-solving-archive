import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M):
  # N >= M이면 1 * ... * M * ... * N = N!이므로 무조건 나눠진다.
  if N >= M:
    return 0
  
  result = 1
  
  for i in range(2, N + 1):
    result = (result * i) % M
  
  return result

if __name__ == "__main__":
  N, M = map(int, input().split())
  
  print(solve(N, M))
  