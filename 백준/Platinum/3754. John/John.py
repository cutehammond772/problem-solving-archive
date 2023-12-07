import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, P):
  result, bitset = 0, 0

  for i in range(N):
    bitset |= P[i]
    result ^= P[i]

  # Case 1. 동일 색상의 M&M 초콜릿이 각각 하나씩 있는 경우,
  # 색상의 수가 홀수이면 선공이 질 수밖에 없다.
  check_01 = (bitset == 1) and result

  # Case 2. 위의 케이스가 아닌 경우, 선공은 어떻게든 위의 상태로 만들 수 있다.
  check_02 = (bitset != 1) and not result

  return not (check_01 or check_02)

if __name__ == "__main__":
  T = int(input())

  for _ in range(T):
    N = int(input())
    A = [*map(int, input().split())]

    result = solve(N, A)

    if result:
      print("John")
    else:
      print("Brother")
