import sys, math
input = lambda: sys.stdin.readline().rstrip()

# 각 1의 위치에 다다르기까지의 1의 누적 합
def accumulations(K):
  result = [1, 2, 5]
  
  for x in range(3, K):
    result.append(2 * (result[-1] - 1) + (2 ** (x - 1)) + 1)
    
  return result

def calc(X, ones):
  result = 0
  
  if X <= 0:
    return 0
    
  for i in range(int(math.log2(X)) + 1):
    if X & (1 << i) > 0:
      result += ones[i] + (X & ((2 ** i) - 1))
    
  return result

if __name__ == '__main__':
  A, B = map(int, input().split())
  ones = accumulations(int(math.log2(B)) + 1)
  
  print(calc(B, ones) - calc(A - 1, ones))
    