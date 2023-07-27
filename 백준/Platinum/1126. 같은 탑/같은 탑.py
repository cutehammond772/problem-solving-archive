import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, B):
  diff = [[0] * 500001 for _ in range(N)]
  diff[0][B[0]] = B[0]

  for x in range(1, N):
    block = B[x]
    
    for k in range(500001):
      if diff[x - 1][k]:
        # Case 1.
        diff[x][k + block] = max(
          diff[x][k + block],
          diff[x - 1][k + block],
          diff[x - 1][k] + block
        )

        # Case 2.
        diff[x][abs(k - block)] = max(
          diff[x][abs(k - block)],
          diff[x - 1][abs(k - block)],
          diff[x - 1][k], (diff[x - 1][k] - k) + block
        )

        # Case 3.
        diff[x][k] = max(diff[x][k], diff[x - 1][k])

    diff[x][block] = max(block, diff[x][block])

  result = diff[N - 1][0]
  return result if result != 0 else -1

if __name__ == '__main__':
  N = int(input())
  B = [*map(int, input().split())]

  print(solve(N, B))
