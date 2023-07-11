import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, invalid, nums):
  for x in nums:
    if x > N // 2:
      break
      
    if not invalid[N - x]:
      return f"{N} = {x} + {N - x}"
    
  return "Goldbach's conjecture is wrong."

def create(N):
  invalid = [False] * (N + 1)
  
  for x in range(2, int(N ** 0.5) + 1):
    if invalid[x]:
      continue
      
    for y in range(x * 2, N + 1, x):
      invalid[y] = True
      
  return invalid, [x for x in range(2, N + 1) if not invalid[x]]

if __name__ == '__main__':
  # 소수 판정, 소수 배열 생성
  invalid, nums = create(1000000)
  
  # 테스트 케이스
  N = int(input())
  
  while N > 4:
    print(solve(N, invalid, nums))
    N = int(input())
