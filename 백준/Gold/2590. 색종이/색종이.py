import sys, math
input = lambda: sys.stdin.readline().rstrip()

# 6x6 : [1칸 / 1판]
def solve_6x6(A):
  need = A[6]

  return need

# 5x5 : [1칸 / 1판] [1x1 11칸]
def solve_5x5(A):
  need = A[5]

  A[1] -= min(A[1], 11 * need)
  return need

# 4x4 : [1칸 / 1판] [2x2 5칸, 1x1 20칸]
def solve_4x4(A):
  need = A[4]

  remain_2x2 = need * 5
  discount = min(A[2], remain_2x2)

  remain_2x2 -= discount
  A[2] -= discount

  # 칸이 일부 남는 경우, 1x1로 채울 수 있다.
  A[1] -= min(A[1], remain_2x2 * 4)

  return need

# 3x3 : [4칸 / 1판] [...]
def solve_3x3(A):
  need = math.ceil(A[3] / 4)

  # 3x3 종이의 개수가 4의 배수가 아니면, 한 판이 일부 비게 된다.
  remain_3x3 = need * 4 - A[3]

  # [3x3 1칸 -> 2x2 1칸, 1x1 5칸]
  if remain_3x3 == 1:
    if A[2] == 0:
      A[1] -= min(A[1], 9)

    else:
      A[2] -= min(A[2], 1)
      A[1] -= min(A[1], 5)

  # [3x3 2칸 -> 2x2 3칸, 1x1 6칸]
  elif remain_3x3 == 2:
    if A[2] == 0:
      A[1] -= min(A[1], 18)

    else:
      A[2] -= min(A[2], 3)
      A[1] -= min(A[1], 6)

  # [3x3 3칸 -> 2x2 5칸, 1x1 7칸]
  elif remain_3x3 == 3:
    if A[2] == 0:
      A[1] -= min(A[1], 27)

    else:
      A[2] -= min(A[2], 5)
      A[1] -= min(A[1], 7)

  return need

# 2x2 : [9칸 / 1판] [...]
def solve_2x2(A):
  need = math.ceil(A[2] / 9)

  # 2x2 종이의 개수가 9의 배수가 아니면, 한 판이 일부 비게 된다.
  remain_2x2 = need * 9 - A[2]
  A[1] -= min(A[1], remain_2x2 * 4)

  return need

# 2x2 : [36칸 / 1판]
def solve_1x1(A):
  need = math.ceil(A[1] / 36)
  return need

def solve(A):
  result = 0

  # 큰 크기의 색종이부터 먼저 채운다.
  result += solve_6x6(A)
  result += solve_5x5(A)
  result += solve_4x4(A)
  result += solve_3x3(A)
  result += solve_2x2(A)
  result += solve_1x1(A)

  return result

if __name__ == '__main__':
  A = [0] * 7

  for x in range(1, 7):
    A[x] = int(input())

  print(solve(A))
