import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = int(1e9 + 7)

# 마지막에 M!을 곱한다.
def solve(N, M, D, T):
  result = 1
  
  for row in range(N):
    T[row].sort()
    
    if row == 0:
      continue
    
    off = 0
    total = 1
    
    for col in range(M):
      # 최대 범위 구하기
      while off < M and T[row][col] + D > T[row - 1][off]:
        off += 1
      
      # 불가능한 경우
      if off <= col:
        return 0
      
      total = (total * (off - col)) % MOD
    
    result = (result * total) % MOD
  
  # M! 곱하기 (처음 한 번이면 된다.)
  for i in range(1, M + 1):
    result = (result * i) % MOD
  
  return result

if __name__ == "__main__":
  N, M, D = map(int, input().split())
  T = [[*map(int, input().split())] for _ in range(N)]
  
  print(solve(N, M, D, T))
  