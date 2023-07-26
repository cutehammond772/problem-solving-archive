import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 10 ** 9 + 7
NUM_RANGE = 10 ** 5 + 1

def update(tree, q, x):
  while 0 < q < len(tree):
    tree[q] += x
    q += q & -q

def query(tree, q):
  result = 0

  while q:
    result += tree[q]
    q -= q & -q

  return result

def solve(N, A):
  if N < 11:
    return 0

  trees = [[0] * NUM_RANGE for _ in range(11 + 1)]

  for x in range(N):
    num = A[x]
    update(trees[1], num, 1)

    for y in range(2, 11 + 1):
      accu = query(trees[y - 1], num - 1) % MOD

      if not accu:
        break

      update(trees[y], num, accu)

  return query(trees[11], NUM_RANGE - 1) % MOD

if __name__ == '__main__':
  N = int(input())
  A = [*map(int, input().split())]

  print(solve(N, A))
