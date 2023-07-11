import sys
input = lambda: sys.stdin.readline().strip()

N = int(input())
nums = [int(input()) for _ in range(N)]

memo = [0] * N

for i in range(N):
  if i < 2:
    memo[i] = sum(nums[:i + 1])
    continue

  if i == 2:
    memo[i] = nums[i] + max(nums[i - 1], nums[i - 2])
    continue
    
  memo[i] = nums[i] + max(nums[i - 1] + memo[i - 3], memo[i - 2])

print(memo[N - 1])