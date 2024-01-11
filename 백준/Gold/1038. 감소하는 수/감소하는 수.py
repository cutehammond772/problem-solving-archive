import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
  if N >= 1023:
    return -1

  nums = []

  for bit in range(1, 1 << 10):
    num = 0

    for i in range(9, -1, -1):
      if bit & 1 << i:
        num = (num * 10) + i

    nums.append(num)

  nums.sort()
  return nums[N]

if __name__ == '__main__':
  N = int(input())
  print(solve(N))
