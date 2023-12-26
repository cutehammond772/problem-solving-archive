import sys
input = lambda: sys.stdin.readline().rstrip()

# 0, 1, 2, ..., X-1, X를 XOR한 값을 도출한다.
def solve(x):
  result, t = 0, 1

  # 첫번째 자리
  result ^= 1 if (x % 4) == 1 or (x % 4) == 2 else 0

  # 두번째 자리부터
  while (1 << t) <= x:
    div = x // (1 << t)
    rem = x % (1 << t)

    result ^= (1 << t) if (div % 2) and ((rem + 1) % 2) else 0
    t += 1

  return result

if __name__ == "__main__":
  A, B = map(int, input().split())
  print(solve(B) ^ solve(A - 1))
