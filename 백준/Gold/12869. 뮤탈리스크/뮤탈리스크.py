import sys
input = lambda: sys.stdin.readline().rstrip()

attacks = [(9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9)]

def solve(N, S):
  memo = [set() for _ in range(max(S) + 1)]
  memo[0].add(tuple(S))
  
  for phase in range(1, max(S) + 1):
    for current in memo[phase - 1]:
      for attack in attacks:
        next = tuple([max(0, current[x] - attack[x]) for x in range(3)])
        
        if next == (0, 0, 0):
          return phase
        
        memo[phase].add(next)
  
  return -1

if __name__ == '__main__':
  N = int(input())
  S = [*map(int, input().split())]
  
  if len(S) < 3:
    S += [0] * (3 - len(S))
  
  print(solve(N, S))
  