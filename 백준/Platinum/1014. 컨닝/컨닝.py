import sys
input = lambda: sys.stdin.readline().rstrip()
mappings = {'.': 0, 'x': 1}

def convert(S):
  result = 0
  
  for x in range(len(S)):
    result |= mappings[S[x]] << x
    
  return result

def solve(N, M, matrix):
  memo = [[0] * (2 ** M) for _ in range(N)]
  
  def adjacent(X):
    for idx in range(1, M):
      if X & (1 << idx) and X & (1 << (idx - 1)):
        return True
      
    return False
  
  def invalid(X, Y):
    for idx in range(M - 1):
      if X & (1 << idx) and Y & (1 << (idx + 1)):
        return True
      
    for idx in range(1, M):
      if X & (1 << idx) and Y & (1 << (idx - 1)):
        return True
      
    return False
  
  def seats(X):
    result = 0
    
    while X:
      result += (X & 1)
      X >>= 1
    
    return result
  
  for row in range(N):
    for mask in range(2 ** M):
      # 1. 앉을 수 없는 자리 체크
      if mask & matrix[row] > 0:
        continue
      
      # 2. 인접한 자리가 선택되었는지 체크
      if adjacent(mask):
        continue
      
      count = seats(mask)
      
      # 3. 첫번째 행인 경우
      if row == 0:
        memo[row][mask] = count
        continue
      
      for previous in range(2 ** M):
        if invalid(previous, mask):
          continue
        
        memo[row][mask] = max(memo[row][mask], count + memo[row - 1][previous])
    
  return max(memo[N - 1])

if __name__ == '__main__':
  C = int(input())
  
  for _ in range(C):
    N, M = map(int, input().split())
    matrix = [convert(input()) for _ in range(N)]
    print(solve(N, M, matrix))
    