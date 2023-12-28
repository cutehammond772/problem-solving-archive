import sys
input = lambda: sys.stdin.readline().rstrip()

# N = 1'000'000인 경우, 1000을 1000개 나열 후 1을 999개 나열하면 된다.
# 위의 케이스로 모든 수가 커버되므로 N은 사실상 의미가 없다.
def solve(N):
  return [1] * 999 + [1000] * 1000

if __name__ == "__main__":
  N = int(input())
  result = solve(N)

  print(len(result))
  print(*result)
