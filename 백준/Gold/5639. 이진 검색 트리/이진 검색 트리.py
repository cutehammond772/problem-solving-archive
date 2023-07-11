import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def input_nodes():
  nodes = []
  temp = input()
  
  while len(temp) > 0:
    nodes.append(int(temp))
    temp = input()
    
  return nodes

def left_size(pre, r, root):
  right = -1
  
  for x in range(*r):
    if pre[x] > root:
      right = x
      break

  # left만 존재하는 경우
  if right == -1:
    return r[1] - r[0] - 1

  return right - r[0] - 1

if __name__ == '__main__':
  # 1. 전위 순회 결과를 입력받는다.
  preorder = input_nodes()
  N = len(preorder)

  # 2. 분할 정복을 이용해 계산 후 후위 순회 배열에 대입한다.
  postorder = [-1] * N
  queue = deque()
  
  # (preorder's offset, postorder's offset, size)
  queue.append((0, 0, N))

  while queue:
    pre_off, post_off, size = queue.popleft()
    
    # root 대입
    root = postorder[post_off + size - 1] = preorder[pre_off]
    
    # left tree의 size 구하기
    left = left_size(preorder, (pre_off, pre_off + size), root)
    
    # left child tree에 대해 수행
    if left > 0:
      queue.append((pre_off + 1, post_off, left))
    
    # right child tree에 대해 수행
    if size - (left + 1) > 0:
      queue.append(((pre_off + 1) + left, post_off + left, size - (left + 1)))
      
  # 3. 결과를 출력한다.
  print(*postorder, sep='\n')