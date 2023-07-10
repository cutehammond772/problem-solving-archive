import sys
from functools import cmp_to_key
input = lambda: sys.stdin.readline().rstrip()

# 벡터의 외적을 통해 방향을 판별한다.
def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
  
  if result > 0:
    return 1
  
  if result < 0:
    return -1
  
  return 0

# 외적을 통해 비교한다.
def compare(x1, y1, x2, y2):
  result = x1 * y2 - x2 * y1
  
  if result != 0:
    return -result
  
  # 외적이 0인 경우, 세 점이 한 직선에 존재한다.
  if x1 != x2:
    return x1 - x2
  
  return y1 - y2

# 그레이엄 스캔을 이용해 볼록 껍질을 찾는다.
def solve(N, dots):
  # 기준점 (x좌표, y좌표가 가장 작은 점 = 껍질에 무조건 포함되는 점)
  dots.sort()
  offset = dots[0]
  
  # 기울기에 따라 정렬한다.
  dots = [offset] + sorted(
    dots[1:],
    key=cmp_to_key(
      lambda p, q: compare(p[0] - offset[0], p[1] - offset[1], q[0] - offset[0], q[1] - offset[1])
    )
  )
  
  stack = [0, 1]
  next = 2
  
  while next < N:
    while len(stack) >= 2:
      second, first = stack.pop(), stack[-1]
      
      x1, y1 = dots[first]
      x2, y2 = dots[second]
      x3, y3 = dots[next]
      
      if ccw(x1, y1, x2, y2, x3, y3) > 0:
        stack.append(second)
        break
    
    stack.append(next)
    next += 1
    
  return len(stack)
  
if __name__ == '__main__':
  N = int(input())
  dots = []
  
  for _ in range(N):
    x, y = map(int, input().split())
    dots.append((x, y))
  
  print(solve(N, dots))
  