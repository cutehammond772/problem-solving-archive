import sys
input = lambda: sys.stdin.readline().rstrip()

def calc(num, op, v):
  if op == '+':
    return num + v

  elif op == '*':
    return num * v

def mark(R, op, v):
  result = [False] * 7

  for num in range(7):
    if not R[num]:
      continue

    result[calc(num, op, v) % 7] = True

  return result

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    N = int(input())

    # 나머지 법칙 이용 : %7 = 0...6만 저장한다.
    memo = [False] * 7

    # K = 1부터 시작한다.
    memo[1] = True

    for _ in range(N):
      op1, v1, op2, v2 = input().split()

      m1 = mark(memo, op1, int(v1))
      m2 = mark(memo, op2, int(v2))

      memo = [m1[num] | m2[num] for num in range(7)]

    if memo[0]:
      print("LUCKY")
    else:
      print("UNLUCKY")
