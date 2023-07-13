import sys, math
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

def create_tree(N, values):
  # 2 ** (ceil(log2N) + 1)
  tree = [0] * (2 ** (math.ceil(math.log2(N)) + 1))
  
  # node는 세그먼트 트리의 노드 번호이다. (값의 순서가 아님)
  def make_tree(node, x, y):
    if x == y:
      tree[node] = values[x]
      return
    
    make_tree(node * 2, x, (x + y) // 2)
    make_tree(node * 2 + 1, (x + y) // 2 + 1, y)
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD
  
  # 루트 노드는 무조건 1이어야 한다.
  make_tree(1, 0, N - 1)
  return tree


# 구하고자 하는 범위는 고정이며,
# 세그먼트 트리의 범위를 잘게 쪼개가며 곱을 구한다.
def query(N, tree, x, y):
  def recursion(node, left, right):
    if x <= left and right <= y:
      return tree[node]
    
    if x > right or y < left:
      return 1
    
    p = recursion(node * 2, left, (left + right) // 2)
    q = recursion(node * 2 + 1, (left + right) // 2 + 1, right)
    return (p * q) % MOD
  
  return recursion(1, 0, N - 1)

def update(N, values, tree, idx, k):
  def recursion(node, left, right):
    if idx < left or idx > right:
      return
    
    if left == right:
      tree[node] = k
      values[idx] = k
      return
    
    recursion(node * 2, left, (left + right) // 2)
    recursion(node * 2 + 1, (left + right) // 2 + 1, right)
    
    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % MOD
  
  recursion(1, 0, N - 1)

if __name__ == '__main__':
  N, M, K = map(int, input().split())
  
  values = [int(input()) for _ in range(N)]
  tree = create_tree(N, values)
  
  for _ in range(M + K):
    C, X, Y = map(int, input().split())
    
    if C == 1:
      update(N, values, tree, X - 1, Y)
    
    if C == 2:
      print(query(N, tree, X - 1, Y - 1))
