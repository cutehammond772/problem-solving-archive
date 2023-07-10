import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 10 ** 9 + 7

def preprocess(N):
  # 온전히 괄호로 덮인 하나의 괄호 문자열
  memo = [0] * (N + 1)
  memo[2] = 1
  
  # 모든 경우의 수
  result = [0] * (N + 1)
  result[2] = 1
  
  for x in range(4, N + 1, 2):
    result[x] = memo[x] = result[x - 2]
    
    for k in range(2, x, 2):
      result[x] = (result[x] + memo[k] * result[x - k]) % MOD
    
  return result

if __name__ == '__main__':
  T = int(input())
  memo = preprocess(5000)
  
  for _ in range(T):
    L = int(input())
    print(memo[L])
    