import sys
input = sys.stdin.readline

R = 1000000007

def solve(k, memo = { 0: 0, 1: 1 }):
  if k not in memo:
    if k % 2 == 1:
      memo[k] = (solve((k + 1) // 2, memo) ** 2 + solve((k - 1) // 2, memo) ** 2) % R
    else:
      memo[k] = (solve(k // 2, memo) * (2 * solve((k // 2) - 1, memo) + solve(k // 2, memo))) % R
    
  return memo[k]

N = int(input())
print(solve(N))