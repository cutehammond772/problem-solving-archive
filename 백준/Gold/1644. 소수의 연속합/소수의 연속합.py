import sys
input = lambda: sys.stdin.readline().rstrip()

def create(N):
  nums = {x for x in range(2, N + 1)}
  for x in range(2, int(N ** 0.5) + 1):
    if x not in nums:
      continue
  
    temp = x * 2
    while temp <= N:
      nums.discard(temp)
      temp += x
  
  return sorted(list(nums))

def solve(N):
  nums = create(N)
  x = 0
  count = 0
  accumulation = 0
  
  for y in range(len(nums)):
    accumulation += nums[y]
    
    if accumulation > N:
      while accumulation > N:
        accumulation -= nums[x]
        x += 1

    if accumulation == N:
      count += 1

  return count

if __name__ == '__main__':
  N = int(input())
  print(solve(N))