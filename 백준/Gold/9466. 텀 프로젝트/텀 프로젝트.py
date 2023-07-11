import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
  checked = set()
  result = 0
  degrees = [0] * N
  
  for node in range(N):
    degrees[node] += 1
    degrees[A[node] - 1] += 1

  for node in range(N):
    if node == A[node] - 1:
      degrees[node] = 0
      checked.add(node)
      result += 1

  departs = [(degrees[node], node) for node in range(N) if degrees[node] == 1]
  
  for depart in departs:
    _, node = depart
    
    counts = [-1] * N
    next, count = A[node] - 1, 0
      
    while node not in checked:
      counts[node] = count
      checked.add(node)
      
      if next in checked and counts[next] >= 0:
        result += counts[node] - counts[next] + 1
        
      node, next, count = next, A[next] - 1, count + 1

  return len(checked) - result

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    
    print(solve(N, A))
