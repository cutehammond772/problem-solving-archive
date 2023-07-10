import sys
sys.setrecursionlimit(10 ** 6)
input = lambda: sys.stdin.readline().rstrip()

def solve(N, A):
  memo = [[1, 0] for _ in range(N + 1)]
  
  def calc(prev, node):
    for next in A[node]:
      if next == prev:
        continue
        
      calc(node, next)
      
      memo[node][0] += min(memo[next])
      memo[node][1] += memo[next][0]
  
  # 1번 노드를 최상위 노드로 정한다.
  calc(0, 1)
  return min(memo[1])

if __name__ == '__main__':
  N = int(input())
  A = [set() for _ in range(N + 1)]
  
  for _ in range(N - 1):
    P, Q = map(int, input().split())
    A[P].add(Q)
    A[Q].add(P)
    
  print(solve(N, A))
  