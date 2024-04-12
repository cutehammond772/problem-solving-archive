import sys
input = lambda: sys.stdin.readline().rstrip()

# factorials
f = [1] * 21

for i in range(1, 21):
  f[i] = i * f[i - 1]

# 1: 수열 구하기
def sequence(N, K):
  result = []
  check = [False] * (N + 1)
  
  for i in range(N - 1, -1, -1):
    for j in range(1, N + 1):
      if check[j]:
        continue
      
      if f[i] < K:
        K -= f[i]
        continue
      
      result.append(j)
      check[j] = True
      break
  
  return result

# 2: 순서 구하기
def order(N, Q):
  result = 1
  check = [False] * (N + 1)
  
  for i in range(N - 1, -1, -1):
    for j in range(1, N + 1):
      if check[j]:
        continue
      
      if j != Q[(N - 1) - i]:
        result += f[i]
        continue
      
      check[j] = True
      break
  
  return result

if __name__ == "__main__":
  N = int(input())
  P, *Q = map(int, input().split())
  
  if P == 1:
    print(*sequence(N, *Q))
  
  elif P == 2:
    print(order(N, Q))
  