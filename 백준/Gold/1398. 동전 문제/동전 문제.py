import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
  result = 0

  # 각 10^(2K+1)의 자리에 대해,
  # 25*(100^K)의 동전을 0~3개 사용했을 때의 경우의 수를 각각 구한다.
  # 왜냐하면, 25원을 사용할 때보다 10원만 사용했을 때 더 최소가 되는 경우가 존재하기 때문이다.
  while N:
    scope = N % 100
    N //= 100

    candidates = []
    
    for x in range(4):
      if scope < 25 * x:
        break

      candidates.append(x + ((scope - 25 * x) // 10) + ((scope - 25 * x) % 10))

    result += min(candidates)

  return result

if __name__ == '__main__':
  T = int(input())

  for _ in range(T):
    N = int(input())
    print(solve(N))
    