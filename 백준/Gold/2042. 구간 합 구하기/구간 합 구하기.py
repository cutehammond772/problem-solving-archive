import sys, math
input = lambda: sys.stdin.readline().rstrip()

REPLACE, SUM = 1, 2

# 세그먼트 트리의 길이
def length(N):
  return 2 ** (math.ceil(math.log2(N)) + 1)

# 세그먼트 트리 생성
def create(nodes):
  result = [0] * length(len(nodes))
  
  def init(x, y, node):
    if x == y:
      result[node] = nodes[x - 1]
    else:
      mid = (x + y) // 2
      result[node] = init(x, mid, node * 2) + init(mid + 1, y, node * 2 + 1)

    return result[node]
    
  init(1, len(nodes), 1)
  return result

# 세그먼트 트리 업데이트
def update(tree, idx, k, lb, rb, node):
  if idx < lb or idx > rb:
    return
    
  tree[node] += k

  if lb != rb:
    update(tree, idx, k, lb, (lb + rb) // 2, node * 2)
    update(tree, idx, k, (lb + rb) // 2 + 1, rb, node * 2 + 1)

# 세그먼트 트리 누적합 구하기
def sum(tree, x, y, lb, rb, node):
  # 범위를 벗어남
  if x > rb or y < lb:
    return 0

  # 범위에 완전히 들어감
  if x <= lb <= rb <= y:
    return tree[node]

  # 범위에 걸치는 경우
  return sum(tree, x, y, lb, (lb + rb) // 2, node * 2) + sum(tree, x, y, (lb + rb) // 2 + 1, rb, node * 2 + 1)

if __name__ == '__main__':
  N, M, K = map(int, input().split())
  
  nodes = [int(input()) for _ in range(N)]
  tree = create(nodes)
  
  for _ in range(M + K):
    command, x, y = map(int, input().split())
    
    if command == REPLACE:
      update(tree, x, y - nodes[x - 1], 1, N, 1)
      nodes[x - 1] = y
      
    if command == SUM:
      print(sum(tree, x, y, 1, N, 1))