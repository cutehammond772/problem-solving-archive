import sys, math
input = lambda: sys.stdin.readline().rstrip()

def upper_bound(A, K):
  x, y = 0, len(A)
  
  while x < y:
    mid = (x + y) // 2
    
    if A[mid] > K:
      y = mid
    else:
      x = mid + 1
  
  return x - 1

def merge(node, left, right):
  L, R = len(left), len(right)
  l_offset, r_offset = 0, 0
  
  for _ in range(L + R):
    if l_offset == L:
      node.append(right[r_offset])
      r_offset += 1
      continue
      
    if r_offset == R:
      node.append(left[l_offset])
      l_offset += 1
      continue
      
    if left[l_offset] <= right[r_offset]:
      node.append(left[l_offset])
      l_offset += 1
    else:
      node.append(right[r_offset])
      r_offset += 1
      
# 머지 소트 트리
def create_tree(N, values):
  # 2 ** (ceil(log2N) + 1)
  tree = [[] for _ in range(2 ** (math.ceil(math.log2(N)) + 1))]
  
  # node는 세그먼트 트리의 노드 번호이다. (값의 순서가 아님)
  def make_tree(node, x, y):
    if x == y:
      tree[node].append(values[x])
      return
    
    make_tree(node * 2, x, (x + y) // 2)
    make_tree(node * 2 + 1, (x + y) // 2 + 1, y)
    merge(tree[node], tree[node * 2], tree[node * 2 + 1])
  
  # 루트 노드는 무조건 1이어야 한다.
  make_tree(1, 0, N - 1)
  return tree

def query(N, tree, x, y, k):
  def recursion(node, left, right):
    if x <= left and right <= y:
      return len(tree[node]) - upper_bound(tree[node], k) - 1
    
    if x > right or y < left:
      return 0
    
    p = recursion(node * 2, left, (left + right) // 2)
    q = recursion(node * 2 + 1, (left + right) // 2 + 1, right)
    return p + q
  
  return recursion(1, 0, N - 1)

if __name__ == '__main__':
  N = int(input())
  values = [*map(int, input().split())]
  tree = create_tree(N, values)
  
  M = int(input())
  for _ in range(M):
    X, Y, K = map(int, input().split())
    print(query(N, tree, X - 1, Y - 1, K))
