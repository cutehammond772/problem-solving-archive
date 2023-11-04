import sys
input = lambda: sys.stdin.readline().rstrip()

# (Decreasing) Monotone Stack
if __name__ == "__main__":
  N = int(input())
  A = [*map(int, input().split())]

  count = [0] * 1000001

  # 등장 횟수 전처리
  for num in A:
    count[num] += 1

  NGF = [-1] * N
  stack = []

  for i in range(N):
    while stack:
      if count[A[stack[-1]]] >= count[A[i]]:
        break

      NGF[stack[-1]] = A[i]
      stack.pop()

    stack.append(i)

  print(*NGF)
