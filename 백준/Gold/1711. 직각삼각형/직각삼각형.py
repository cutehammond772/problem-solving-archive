import sys
input = lambda: sys.stdin.readline().rstrip()
  
def check(d, d1, d2):
  return (d1[0] - d[0]) * (d2[0] - d[0]) == -(d1[1] - d[1]) * (d2[1] - d[1])

if __name__ == '__main__':
  N = int(input())
  D = [[0, 0] for _ in range(N)]
  result = 0
  
  for idx in range(N):
    x, y = map(int, input().split())
    D[idx][0], D[idx][1] = x, y

  for p in range(N):
    for q in range(p + 1, N):
      for r in range(q + 1, N):
        if check(D[p], D[q], D[r]) or check(D[q], D[p], D[r]) or check(D[r], D[p], D[q]):
          result += 1
    
  print(result)