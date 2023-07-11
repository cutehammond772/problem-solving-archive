import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, nums):
  result = []
  temp = []
  
  def make(offset, count):
    if count == M:
      result.append(tuple(temp))
      return
    
    for x in range(offset, N):
      temp.append(nums[x])
      make(x + 1, count + 1)
      temp.pop()
      
  make(0, 0)
  return result

if __name__ == '__main__':
  N, M = map(int, input().split())
  nums = [*map(int, input().split())]
  
  # 오름차순으로 정렬을 진행한다.
  nums.sort()
  result = solve(N, M, nums)
  
  for combination in result:
    print(*combination)