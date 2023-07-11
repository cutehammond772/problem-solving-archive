import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  M = [[0] * N for _ in range(2)]
  result = 0
  
  for k in range(N):
    M[0][k], M[1][k] = map(int, input().split())
    
  for k in range(N):
    p, q = k, (k + 1) % N
    result += M[0][p] * M[1][q] - M[0][q] * M[1][p]
    
  print('{:.1f}'.format(abs(result / 2)))