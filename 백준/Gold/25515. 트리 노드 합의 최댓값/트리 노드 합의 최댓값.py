import sys
sys.setrecursionlimit(101010)
input = lambda: sys.stdin.readline().rstrip()

def solve(tree, memo):
  def query(node):
    for next in tree[node]:
      cost = query(next)

      if cost > 0:
        memo[node] += cost

    return memo[node]

  return query(0)

if __name__ == "__main__":
  N = int(input())
  tree = [[] for _ in range(N)]

  for _ in range(N - 1):
    p, c = map(int, input().split())
    tree[p].append(c)

  memo = [*map(int, input().split())]
  print(solve(tree, memo))
