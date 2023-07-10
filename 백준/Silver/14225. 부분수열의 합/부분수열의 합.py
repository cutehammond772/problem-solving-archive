import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(S, Q):
  memo = [False] * 2000001
  
  for x in range(2 ** S):
    total, offset = 0, 0
    
    while x:
      if x & 1:
        total += Q[offset]
      
      x >>= 1
      offset += 1
    
    memo[total] = True
  
  return memo.index(False)

if __name__ == '__main__':
  S = int(input())
  sequence = [*map(int, input().split())]
  
  print(solve(S, sequence))
  