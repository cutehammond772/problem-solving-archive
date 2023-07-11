import sys
from itertools import combinations
input = lambda: sys.stdin.readline().rstrip()

def solve(N, vertices, total):
  total_x, total_y = total
  result = 2 ** 63 - 1
  
  for combs in combinations(range(N), N // 2):
    accu_x, accu_y = 0, 0
    
    for vertex in combs:
      x, y = vertices[vertex]
      accu_x += x
      accu_y += y
      
    result = min(
      result,
      (((total_x - 2 * accu_x) ** 2) + ((total_y - 2 * accu_y) ** 2)) ** 0.5
    )
    
  return result
  
if __name__ == '__main__':
  T = int(input())
  
  for _ in range(T):
    N = int(input())
    vertices = []
    total_x, total_y = 0, 0
    
    for _ in range(N):
      x, y = map(int, input().split())
      
      total_x += x
      total_y += y
      vertices.append((x, y))
      
    print(solve(N, vertices, (total_x, total_y)))
    