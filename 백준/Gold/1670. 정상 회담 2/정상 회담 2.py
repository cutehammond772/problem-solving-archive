import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 987654321

def solve(N):
  # 홀수이면 짝을 지을 수 없다.
  if N % 2:
    return 0
  
  memo = [0] * (N + 1)
  
  # 두 칸만 남은 경우 한 가지만 가능하다.
  memo[0] = memo[2] = 1
  
  for x in range(4, N + 1, 2):
    result = 0
    a, b = 0, x - 2
    
    while a <= b:
      combination = memo[a] * memo[b] << (a != b)
      result = (result + combination % MOD) % MOD
      a += 2; b -= 2
    
    memo[x] = result
  
  return memo[N]

if __name__ == "__main__":
  N = int(input())
  print(solve(N))
  