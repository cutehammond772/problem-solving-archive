import sys
input = lambda: sys.stdin.readline().rstrip()

# 모두 중앙에 있는 경우: 1가지
# 하나는 중앙, 하나는 중앙이 아닌 자리에 있는 경우: 4가지(4C1)
# 둘 다 중앙이 아닌 자리에 있는 경우: 6가지 (4C2)

NaN = 400001
UP, LEFT, DOWN, RIGHT = 1 << 0, 1 << 1, 1 << 2, 1 << 3

ADJACENTS = {}
ADJACENTS[UP] = ADJACENTS[DOWN] = LEFT | RIGHT
ADJACENTS[LEFT] = ADJACENTS[RIGHT] = UP | DOWN

OPPOSITES = {}
OPPOSITES[UP] = DOWN
OPPOSITES[DOWN] = UP
OPPOSITES[LEFT] = RIGHT
OPPOSITES[RIGHT] = LEFT

def count(x):
  result = 0
  
  for t in range(4):
    if x & (1 << t) > 0:
      result += 1
      
  return result

def solve(commands):
  memo = [[NaN] * 16 for _ in range(len(commands))]
  memo[0][1 << commands[0]] = 2
  
  for x in range(1, len(commands)):
    cmd = 1 << commands[x]
    
    for t in range(16):
      prev = memo[x - 1][t]
      
      if prev == NaN:
        continue
      
      if t & cmd > 0: # 1. 이미 이전 단계에서 발판이 겹칠 때
        memo[x][t] = min(memo[x][t], prev + 1)
      else: # 2. 발판이 겹치지 않을 때
        if count(t) == 1: # 2-1. 하나는 중앙에 있을 때
          # 2-1-1. 중앙의 발을 이동시킬 때
          memo[x][t | cmd] = min(memo[x][t | cmd], prev + 2)
            
          # 2-1-2. 기존에 있던 발을 이동할 때
          if ADJACENTS[cmd] & t > 0:
            memo[x][cmd] = min(memo[x][cmd], prev + 3)
          else:
            memo[x][cmd] = min(memo[x][cmd], prev + 4)
        # 2-2. 둘 다 중앙에 있지 않을 때
        elif count(t) == 2:
          # 2-2-1. 두 발판이 서로 인접해 있는 경우
          if count(ADJACENTS[cmd] & t) == 1:
            # 2-2-1-1. 인접한 자리로 이동할 때
            memo[x][t ^ (ADJACENTS[cmd] & t) | cmd] = min(
              memo[x][t ^ (ADJACENTS[cmd] & t) | cmd],
              prev + 3
            )
              
            # 2-2-1-2. 반대편 자리로 이동할 때
            memo[x][t ^ OPPOSITES[cmd] | cmd] = min(
              memo[x][t ^ OPPOSITES[cmd] | cmd],
              prev + 4
            )
          # 2-2-2. 두 발판이 서로 떨어져 있는 경우
          else:
            # 2-2-2-1. 인접한 자리로 이동할 때 (반대편 자리로 이동하는 경우 없음)
            v, w = (1 << x for x in range(4) if (t & (1 << x)) > 0)
            
            memo[x][cmd | v] = min(memo[x][cmd | v], prev + 3)
            memo[x][cmd | w] = min(memo[x][cmd | w], prev + 3)

  return min(memo[len(commands) - 1])

if __name__ == '__main__':
  *commands, _ = map(lambda x: int(x) - 1, input().split())
  print(solve(commands))