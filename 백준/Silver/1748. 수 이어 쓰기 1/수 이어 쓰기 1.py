import sys, math
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
  result = 0
  top = math.floor(math.log10(N))
  
  # 최상위 자리수에 도달하기 전
  for x in range(top):
    result += (x + 1) * ((10 ** (x + 1)) - (10 ** x))
  
  # 최상위 자리수에 도달한 후
  highest = N // (10 ** top)
  result += (top + 1) * ((10 ** top) * (highest - 1) + N % (10 ** top) + 1)
  
  return result

if __name__ == '__main__':
  N = int(input())
  print(solve(N))
