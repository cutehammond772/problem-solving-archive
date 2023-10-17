import sys
input = lambda: sys.stdin.readline().rstrip()

def resolve(X, Y):
  result = dict()

  for i in X:
    for j in Y:
      if i + j in result: result[i + j] += 1
      else: result[i + j] = 1

  return result

if __name__ == "__main__":
  N = int(input())
  A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N

  for x in range(N):
    A[x], B[x], C[x], D[x] = map(int, input().split())

  Q = resolve(C, D)
  count = 0

  for x in A:
    for y in B:
      if -(x + y) in Q:
        count += Q[-(x + y)]

  print(count)
