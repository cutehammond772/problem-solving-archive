import sys
input = lambda: sys.stdin.readline().rstrip()
MOD = 1_000_000_007

def solve(N, menus):
  result = 0
  menus.sort()

  for x in range(N):
    result = (result + menus[x] * (2 ** x - 2 ** ((N - 1) - x))) % MOD
  
  return result

if __name__ == '__main__':
  N = int(input())
  menus = [*map(int, input().split())]
  
  print(solve(N, menus))