import sys
from heapq import heapify, heappop
input = lambda: sys.stdin.readline().rstrip()

if __name__ == "__main__":
  N = int(input())
  S = input()

  heap = [(S[x], -x) for x in range(N)]
  heapify(heap)

  # 상근, 희원
  A, B = [], []
  checked = [False] * N

  a_index = N - 1

  for _ in range(N >> 1):
    # 상근
    while checked[a_index]:
      a_index -= 1

    A.append(S[a_index])
    checked[a_index] = True
    a_index -= 1

    # 희원
    while heap and checked[-heap[0][1]]:
      heappop(heap)

    Q, b_idx = heappop(heap)
    checked[-b_idx] = True
    B.append(Q)

  A, B = "".join(A), "".join(B)

  print("NE" if A <= B else "DA")
  print(B)
