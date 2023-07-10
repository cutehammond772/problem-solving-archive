import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, K, S):
  memo = [0] * (K + 1)
  memo[0] = 1
  
  for x in range(N):
    for k in range(S[x], K + 1):
      if not k % S[x]:
        memo[k] += 1
        memo[k] += memo[k - S[x]] - 1
      else:
        memo[k] += memo[k - S[x]]
        
  return memo[K]

if __name__ == '__main__':
  N, K = map(int, input().split())
  sequence = [int(input()) for _ in range(N)]
  
  print(solve(N, K, sequence))
