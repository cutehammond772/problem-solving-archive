import sys, math
input = lambda: sys.stdin.readline().rstrip()
MIN, MAX = 0, 10 ** 9 + 1

def analyze(N, sequences):
  D = int(math.log2(N)) + 2
  accumulations = [[[MAX, MIN] for _ in range(D)] for _ in range(N)]
  
  for idx in range(N):
    current = sequences[idx]
    accumulations[idx][0] = [current, current]
    
    for k in range(1, D):
      ancestor = idx - (2 ** (k - 1))
      
      if ancestor < 0:
        break
        
      A1 = accumulations[idx][k - 1]
      A2 = accumulations[ancestor][k - 1]
      
      accumulations[idx][k] = [min(A1[0], A2[0]), max(A1[1], A2[1])]
  
  def solve(A, B):
    if A == B:
      return accumulations[A][0]
    
    result = [MAX, MIN]
    
    for idx in range(D - 1, -1, -1):
      if B - (2 ** idx - 1) < A:
        continue
      
      next = accumulations[B][idx]
      B -= 2 ** idx
      result = [min(result[0], next[0]), max(result[1], next[1])]
    
    return result
  
  return solve

if __name__ == '__main__':
  N, M = map(int, input().split())
  sequences = [int(input()) for _ in range(N)]
  solve = analyze(N, sequences)
  
  for _ in range(M):
    A, B = map(int, input().split())
    print(*solve(A - 1, B - 1))
    