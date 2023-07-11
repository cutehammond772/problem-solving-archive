import sys
input = sys.stdin.readline

N = int(input().strip())
nums = sorted([int(input().strip()) for _ in range(N)])

mid = nums[N // 2]
ran = nums[-1] - nums[0]
summary = 0
freq, max_freq, temp_freq = [], 0, 0

for i in range(N):
  summary += nums[i]

  if i == 0:
    temp_freq = 1
  else:
    if nums[i - 1] == nums[i]:
      temp_freq += 1
    else:
      if max_freq < temp_freq:
        max_freq = temp_freq
        freq = [nums[i - 1]]
      elif max_freq == temp_freq:
        freq.append(nums[i - 1])
        
      temp_freq = 1

# 마지막 수에 대한 최빈값 처리
if max_freq < temp_freq:
  max_freq = temp_freq
  freq = [nums[i - 1]]
elif max_freq == temp_freq:
  freq.append(nums[i - 1])

summary = round(summary / N)
freq = freq[0] if len(freq) < 2 else freq[1]

print(summary)
print(mid)
print(freq)
print(ran)