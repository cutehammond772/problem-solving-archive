import sys, math
input = lambda: sys.stdin.readline().rstrip()

def cumulate(N, memo):
  result = [0] * 10
  
  if N == 0:
    return result
    
  L = math.floor(math.log10(N)) + 1
  top = [0] * L
  
  for x in range(L - 1, -1, -1):
    y = N // (10 ** x) % 10

    if y == 0:
      continue
      
    # 반복하여 등장하는 상위 숫자에 대해 처리
    if top[L - 1] > 0:
      for z in range(L):
        if z > x:
          result[top[z]] += y * (10 ** x)
        else:
          result[top[z]] += (10 ** z) - 1

    # [~y00000...]의 숫자의 빈도 누적하기
    for k in range(10):
      result[k] += memo[x][y][k]

    # 상위 숫자로 추가
    top[x] = y
    
  return result

def solve(N):
  L = math.floor(math.log10(N)) + 1
  memo = [[[0] * 10 for _ in range(10)] for _ in range(L)]
  
  for x in range(L):
    for y in range(1, 10):
      memo[x][y] = cumulate(y * (10 ** x) - 1, memo)
      
      memo[x][y][y] += 1
      memo[x][y][0] += x

  return cumulate(N, memo)

if __name__ == '__main__':
  N = int(input())
  
  print(*solve(N))