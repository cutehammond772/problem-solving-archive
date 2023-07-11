import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, S):
  # 특정 숫자를 끝으로 하는 수열의 최대 길이
  nums = [0] * 1001
  # 각 인덱스의 원소를 끝으로 하는 최장 증가 수열의 최대 길이
  result = [1] * N

  for x in range(N):
    K = S[x]
    result[x] = max(result[x], max(nums[:K]) + 1)
    nums[K] = max(nums[K], result[x])
    
  return result

if __name__ == '__main__':
  N = int(input())
  S = list(map(int, input().split()))
  
  forward = solve(N, S)
  backward = solve(N, S[::-1])[::-1]

  print(max([forward[x] + backward[x] - 1 for x in range(N)]))