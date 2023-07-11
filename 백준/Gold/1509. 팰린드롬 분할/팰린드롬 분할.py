import sys
input = lambda: sys.stdin.readline().rstrip()

NaN = 2501

def palindromes(S, L):
  memo = [[NaN] * L for _ in range(L)]
  
  for x in range(L):
    # 자기 자신은 팰린드롬
    memo[x][x] = 1

    # 홀수 크기의 팰린드롬
    for y in range(1, min(x + 1, L - x)):
      if S[x - y] != S[x + y]:
        break
        
      memo[x - y][x + y] = 1

    # 짝수 크기의 팰린드롬
    for y in range(min(x + 1, L - x - 1)):
      if S[x - y] != S[x + y + 1]:
        break
        
      memo[x - y][x + y + 1] = 1
      
  return memo

def solve(S, L):
  memo = [[NaN] * L for _ in range(L)]
  data = palindromes(S, L)
  
  memo[0][0] = 1
  
  for x in range(L):
    for k in range(x):
      memo[0][x] = min(
        memo[0][x], data[0][x],
        memo[0][k] + min(data[k + 1][x], memo[k + 1][x])
      )

  return memo[0][L - 1]
    
if __name__ == '__main__':
  S = input()
  L = len(S)

  print(solve(S, L))