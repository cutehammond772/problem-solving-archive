import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  K = [*map(int, input().split())]

  # 이상
  A1 = [0] * 500001

  # 이하
  A2 = [0] * 500001

  for num in K:
    if num > 0:
      A1[num] += 1
    else:
      A2[-num] += 1

  # 누적 합
  for i in range(1, 500001):
    A1[i] += A1[i - 1]
    A2[500000 - i] += A2[500001 - i]

  result = []

  for i in range(500001):
    if N - (A1[i] + A2[i]) == i:
      result.append(i)

  print(len(result))
  print(*result)
