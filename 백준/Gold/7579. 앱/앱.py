import sys
input = lambda: sys.stdin.readline().rstrip()

NaN = 10 ** 7 + 1

def solve(N, M, apps):
  arr = [[0] * 10001 for _ in range(N + 1)]
  result = NaN
  
  for i in range(1, N + 1):
    for w in range(10001):
      size, cost = apps[i - 1]
      
      if w >= cost:
        arr[i][w] = max(arr[i - 1][w], arr[i - 1][w - cost] + size)
        
        if arr[i][w] >= M:
          result = min(result, w)
          
      else:
        arr[i][w] = arr[i - 1][w]

  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  S = list(map(int, input().split()))
  C = list(map(int, input().split()))

  apps = [(S[x], C[x]) for x in range(N)]
  print(solve(N, M, apps))