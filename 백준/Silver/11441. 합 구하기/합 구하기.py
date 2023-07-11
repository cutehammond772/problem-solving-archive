import sys
input = lambda: sys.stdin.readline().rstrip()

def accumulate():
  memo = [0]
  
  for num in input().split():
    memo.append(memo[-1] + int(num))
    
  return memo

if __name__ == '__main__':
  _ = input()
  accumulations = accumulate()
  
  M = int(input())
  for _ in range(M):
    I, J = map(int, input().split())
    print(accumulations[J] - accumulations[I - 1])