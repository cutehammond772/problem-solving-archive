import sys, math
input = lambda: sys.stdin.readline().rstrip()

def make(N, values):
  S = 2 ** (math.ceil(math.log2(N)) + 1)
  sequences = [[] for _ in range(S)]
  tree = [0] * S
  
  def recursion(node, left, right):
    if left == right:
      tree[node] = 0
      sequences[node].append(values[left])
      return
    
    recursion(node * 2, left, (left + right) // 2)
    recursion(node * 2 + 1, (left + right) // 2 + 1, right)
    
    # 병합 과정
    count = 0
    Q0, Q1 = sequences[node * 2], sequences[node * 2 + 1]
    N0, L0 = 0, len(Q0)
    N1, L1 = 0, len(Q1)
    
    for _ in range(L0 + L1):
      if N0 == L0:
        sequences[node].append(Q1[N1])
        N1 += 1
        continue
      
      if N1 == L1:
        sequences[node].append(Q0[N0])
        N0 += 1
        continue
      
      if Q0[N0] > Q1[N1]:
        sequences[node].append(Q1[N1])
        count += L0 - N0
        N1 += 1
      else:
        sequences[node].append(Q0[N0])
        N0 += 1
    
    tree[node] = count + tree[node * 2] + tree[node * 2 + 1]
  
  recursion(1, 0, N - 1)
  return tree

if __name__ == '__main__':
  N = int(input())
  values = [*map(int, input().split())]
  tree = make(N, values)
  
  print(tree[1])
  