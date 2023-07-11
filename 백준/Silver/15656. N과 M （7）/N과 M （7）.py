import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, nums):
  result = []
  temp = []
  
  def make(count):
    if count == M:
      result.append(tuple(temp))
      return
    
    for x in range(N):
      temp.append(nums[x])
      make(count + 1)
      temp.pop()
      
  make(0)
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  nums = [*map(int, input().split())]
  
  # 오름차순으로 정렬을 진행한다.
  nums.sort()
  result = solve(N, M, nums)
  
  for combination in result:
    print(*combination)