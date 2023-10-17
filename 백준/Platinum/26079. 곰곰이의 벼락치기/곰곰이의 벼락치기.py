import sys
sys.setrecursionlimit(10 ** 6)

input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

def factorials(N):
  result = [1]

  for x in range(1, N + 1):
    result.append((result[-1] * x) % MOD)

  return result

def pow(x, p):
  result = 1

  while p:
    if p & 1:
      result = (result * x) % MOD

    p >>= 1
    x = (x ** 2) % MOD

  return result

def solve(N, R, adj):
  memo, nodes = [0] * (N + 1), [0] * (N + 1)
  F = factorials(N)

  def combination(sub_nodes):
    result = F[sum(sub_nodes)]

    for nodes in sub_nodes:
      result = (result * pow(F[nodes], MOD - 2)) % MOD

    return result

  def traverse(node):
    sub_nodes = []
    sub_combinations = 1

    for next in adj[node]:
      traverse(next)

      sub_nodes.append(nodes[next])
      sub_combinations = (sub_combinations * memo[next]) % MOD

    nodes[node], memo[node] = sum(sub_nodes) + 1, (combination(sub_nodes) * sub_combinations) % MOD

  total_combinations = 1
  total_nodes = []

  for root in R:
    traverse(root)

    total_nodes.append(nodes[root])
    total_combinations = (total_combinations * memo[root]) % MOD

  return (combination(total_nodes) * total_combinations) % MOD

if __name__ == "__main__":
  N, M = map(int, input().split())

  # 선행 강의가 존재하지 않는 강의를 찾는다.
  root = [True] * (N + 1)
  adj = [[] for _ in range(N + 1)]

  for _ in range(M):
    a, b = map(int, input().split())

    adj[a].append(b)
    root[b] = False

  print(solve(N, [x for x in range(1, N + 1) if root[x]], adj))
