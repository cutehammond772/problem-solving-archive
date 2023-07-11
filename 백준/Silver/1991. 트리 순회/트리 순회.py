# 상수
ROOT_NODE = 'A'
NO_CHILD = '.'
LEFT, RIGHT = 0, 1

def lf(fn, *args):
  fn(*args)
  print()
  
def root_fn(node):
  print(node, end='')

def left_fn(node, nodes, traversal):
  if nodes[node][LEFT] != NO_CHILD:
    traversal(nodes[node][LEFT], nodes)

def right_fn(node, nodes, traversal):
  if nodes[node][RIGHT] != NO_CHILD:
    traversal(nodes[node][RIGHT], nodes)
    
# 전위 순회
def preorder(node, nodes):
  root_fn(node)
  left_fn(node, nodes, preorder)
  right_fn(node, nodes, preorder)

# 중위 순회
def inorder(node, nodes):
  left_fn(node, nodes, inorder)
  root_fn(node)
  right_fn(node, nodes, inorder)

# 후위 순회
def postorder(node, nodes):
  left_fn(node, nodes, postorder)
  right_fn(node, nodes, postorder)
  root_fn(node)

if __name__ == '__main__':
  N = int(input())
  nodes = {}
  
  for _ in range(N):
    node, left, right = input().split()
    nodes[node] = [left, right]
  
  lf(preorder, ROOT_NODE, nodes)
  lf(inorder, ROOT_NODE, nodes)
  lf(postorder, ROOT_NODE, nodes)