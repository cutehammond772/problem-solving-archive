import sys
from queue import Queue
input = lambda: sys.stdin.readline().strip()

def solve(inorder, postorder, preorder):
  que = Queue()
  
  # (...inorder's boundary, ...postorder's boundary, preorder's offset)
  que.put((0, len(inorder), 0, len(postorder), 0))
    
  # indexing
  indexes = [-1] * (len(inorder) + 1)
  
  for index in range(len(inorder)):
    indexes[inorder[index]] = index
    
  while not que.empty():
    in_start, in_end, post_start, post_end, pre_offset = que.get()
    
    root = postorder[post_end - 1]
    root_idx = indexes[root] - in_start
    
    preorder[pre_offset] = root
    
    if root_idx != 0:
      que.put((in_start, in_start + root_idx, post_start, post_start + root_idx, pre_offset + 1))
      
    if in_start + root_idx + 1 != in_end:
      que.put((in_start + root_idx + 1, in_end, post_start + root_idx, post_end - 1,
               pre_offset + root_idx + 1))

if __name__ == '__main__':
  N = int(input())
  
  inorder = list(map(int, input().split()))
  postorder = list(map(int, input().split()))
  preorder = [-1] * N
  
  solve(inorder, postorder, preorder)
  print(*preorder)