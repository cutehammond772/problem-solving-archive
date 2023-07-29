import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  N = int(input())
  nums = [[x, len(x)] for x in input().split()]

  for idx in range(N):
    nums[idx][0] *= (10 // nums[idx][1]) + 1

  nums.sort(key=lambda x: x[0], reverse=True)
  result = "".join([num[0][:num[1]] for num in nums])

  print(result if int(result) else 0)
