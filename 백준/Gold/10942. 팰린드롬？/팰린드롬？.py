import sys
input = lambda: sys.stdin.readline().rstrip()

ODD, EVEN = 0, 1

def resolve(N, A):
  R = [[[0] * N, [0] * N] for _ in range(N)]
  
  for x in range(N):
    # ODD
    for t in range(min(x + 1, N - x)):
      if A[x - t] != A[x + t]:
        break
        
      R[x][ODD][t] = 1
      
    # EVEN
    for t in range(min(x + 1, N - x - 1)):
      if A[x - t] != A[(x + 1) + t]:
        break
        
      R[x][EVEN][t] = 1
  
  return R    

def solve(N, R, x, y):
  dist = y - x
  
  if dist % 2 == 1:
    # 짝수 길이의 팰린드롬
    return R[x + dist // 2][EVEN][(dist - 1) // 2]
  else:
    # 홀수 길이의 팰린드롬
    return R[x + dist // 2][ODD][dist // 2]

if __name__ == '__main__':
  N = int(input())
  A = list(map(int, input().split()))
  R = resolve(N, A)
  
  T = int(input())
  for _ in range(T):
    A, B = map(int, input().split())
    print(solve(N, R, A - 1, B - 1))

