import sys
input = lambda: sys.stdin.readline().rstrip()

def find(U, x):
  if U[x] == x:
    return x

  T = [x]

  while U[T[-1]] != T[-1]:
    T.append(U[T[-1]])

  for n in T:
    U[n] = T[-1]

  return U[x]

def union(U, x, y):
  x, y = find(U, x), find(U, y)

  if x <= y:
    U[y] = U[x]
  else:
    U[x] = U[y]

if __name__ == "__main__":
  N, M = map(int, input().split())

  # 분리 집합
  U = [x for x in range(N + 1)]

  for _ in range(M):
    op, a, b = map(int, input().split())

    if op == 0:
      union(U, a, b)
    elif op == 1:
      print("YES" if find(U, a) == find(U, b) else "NO")
      