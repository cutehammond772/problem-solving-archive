from queue import Queue
import sys
input = lambda: sys.stdin.readline().strip()

# 특정 지점으로부터의 최대값
def solve(tree, x):
  max_val, max_idx = 0, -1
  
  visited = set()
  que = Queue()
  que.put((x, 0))
  
  while not que.empty():
    curr, cost = que.get()
    visited.add(curr)

    if len(tree[curr]) == 1 and curr != x:
      if max_val < cost:
        max_val, max_idx = cost, curr
        continue
        
    for next in tree[curr]:
      if next in visited:
        continue
      
      que.put((next, cost + tree[curr][next]))
      
  return max_val, max_idx
  
# 입력
if __name__ == '__main__':
  N = int(input())
  tree = [{} for _ in range(N)]
  
  for x in range(N - 1):
    curr, next, cost = map(int, input().split())
    tree[curr - 1][next - 1] = tree[next - 1][curr - 1] = cost
      
  _, first_idx = solve(tree, 0)
  result_val, _ = solve(tree, first_idx)
  print(result_val)
