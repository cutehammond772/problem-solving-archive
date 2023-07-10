import sys, math
input = lambda: sys.stdin.readline().rstrip()

def solve(N):
  result = 0
  
  for x in range(1, int(math.log(N, 5)) + 1):
    result += N // (5 ** x)
  
  return result

if __name__ == '__main__':
  T = int(input())
  
  for _ in range(T):
    x = int(input())
    print(solve(x))
