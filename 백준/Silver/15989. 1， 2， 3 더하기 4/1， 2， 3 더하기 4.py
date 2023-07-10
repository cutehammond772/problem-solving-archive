import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
  T = int(input())
  memo = [1] * 10001
  
  for x in range(1, 10001):
    memo[x] += (x // 2) + (x // 3)
    
    for k in range(3, x + 1, 3):
      memo[x] += (x - k) // 2
  
  for _ in range(T):
    N = int(input())
    print(memo[N])
