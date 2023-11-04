import sys
input = lambda: sys.stdin.readline().rstrip()

# (Decreasing) Monotone Stack
def solve(N, A):
  count = [0] * 1000001

  # 등장 횟수 전처리
  for num in A:
    count[num] += 1

  NGF = [-1] * N
  stack = [(A[0], 0)]

  for i in range(1, N):
    curr_num, curr_idx = A[i], i

    while stack:
      prev_num, prev_idx = stack[-1]

      if count[prev_num] >= count[curr_num]:
        break

      NGF[prev_idx] = curr_num
      stack.pop()

    stack.append((curr_num, curr_idx))

  return NGF

if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]

  NGF = solve(N, A)
  print(*NGF)
