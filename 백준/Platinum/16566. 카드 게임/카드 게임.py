import sys
input = lambda: sys.stdin.readline().rstrip()

def index(A, K):
  x, y = 0, len(A)
  
  while x < y:
    mid = (x + y) // 2
    
    if A[mid] > K:
      y = mid
    else:
      x = mid + 1
      
  return x

def find(U, x):
  if U[x] == x:
    return U[x]

  nodes = [x]
  while U[nodes[-1]] != nodes[-1]:
    nodes.append(U[nodes[-1]])

  for node in nodes:
    U[node] = nodes[-1]
    
  return U[x]

def solve(M, K, nums, target):
  U = [x for x in range(M)]
  result = []
  
  for k in range(K):
    idx = find(U, index(nums, target[k]))
    result.append(nums[idx])

    U[idx] = idx + 1

  return result

if __name__ == '__main__':
  _, M, K = map(int, input().split())
  nums = sorted(list(map(int, input().split())))
  target = list(map(int, input().split()))

  print(*solve(M, K, nums, target), sep = '\n')
