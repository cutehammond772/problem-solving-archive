import sys
input = lambda: sys.stdin.readline().rstrip()

def lower_bound(A, K):
  x, y = 0, len(A)
  
  while x < y:
    mid = (x + y) // 2

    if A[mid] >= K:
      y = mid
    else:
      x = mid + 1

  return x

def solve(N, P):
  memo, indexes = [P[0][1]], [0]
  result = { P[x][0] for x in range(N) }
  
  for x in range(1, N):
    if memo[-1] < P[x][1]:
      indexes.append(len(memo))
      memo.append(P[x][1])
      continue
      
    idx = lower_bound(memo, P[x][1])
    
    memo[idx] = P[x][1]
    indexes.append(idx)

  offset = len(memo) - 1
  
  for x in range(N - 1, -1, -1):
    if offset < 0:
      break
      
    if indexes[x] == offset:
      result.remove(P[x][0])
      offset -= 1
  
  return N - len(memo), list(sorted(result))
    

if __name__ == '__main__':
  N = int(input())
  P = []
  
  for _ in range(N):
    A, B = map(int, input().split())
    P.append((A, B))

  P.sort()
  
  count, result = solve(N, P)
  
  print(count)
  print(*result, sep = '\n')