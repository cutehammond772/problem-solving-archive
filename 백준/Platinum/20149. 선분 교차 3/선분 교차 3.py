import sys
input = lambda: sys.stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1)
  return 1 if result > 0 else -1 if result < 0 else 0

def compare(x1, y1, x2, y2):
  if x1 == x2:
    return y2 - y1
    
  return x2 - x1

if __name__ == '__main__':
  x1, y1, x2, y2 = map(int, input().split())
  x3, y3, x4, y4 = map(int, input().split())
  
  L1x, L1y = ccw(x1, y1, x2, y2, x3, y3), ccw(x1, y1, x2, y2, x4, y4)
  L2x, L2y = ccw(x3, y3, x4, y4, x1, y1), ccw(x3, y3, x4, y4, x2, y2)
  L1, L2 = L1x * L1y, L2x * L2y
  
  # 일부가 겹치는 경우 OR 끝점끼리 만나는 경우
  if L1 == L2 == 0:
    if compare(x1, y1, x2, y2) < 0:
      x1, x2 = x2, x1
      y1, y2 = y2, y1

    if compare(x3, y3, x4, y4) < 0:
      x3, x4 = x4, x3
      y3, y4 = y4, y3

    if compare(x1, y1, x4, y4) >= 0 and compare(x3, y3, x2, y2) >= 0:
      print(1)
      
      # 한 끝점에서 만나는 경우 (1)
      if not (L1x == L1y == L2x == L2y == 0):
        if (x1, y1) == (x3, y3) or (x1, y1) == (x4, y4):
          print(x1, y1)
          
        elif (x2, y2) == (x3, y3) or (x2, y2) == (x4, y4):
          print(x2, y2)
          
      # 한 끝점에서 만나는 경우 (2)
      elif compare(x1, y1, x4, y4) > 0 and compare(x3, y3, x2, y2) == 0:
        print(x2, y2)

      # 한 끝점에서 만나는 경우 (3)
      elif compare(x1, y1, x4, y4) == 0 and compare(x3, y3, x2, y2) > 0:
        print(x1, y1)
      
    else:
      print(0)
      
  elif L1 <= 0 and L2 <= 0:
    print(1)

    # 두 선분 모두 y축에 평행하지 않은 경우 (1)
    if x1 != x2 and x3 != x4:
      a1, a2 = (y2 - y1) / (x2 - x1), (y4 - y3) / (x4 - x3)
      b1, b2 = y1 - a1 * x1, y3 - a2 * x3
        
      x = (b2 - b1) / (a1 - a2)
      y = a1 * x + b1
        
    # 한 선분이 y축에 평행한 경우 (2)
    elif x1 == x2 and x3 != x4:
      a2 = (y4 - y3) / (x4 - x3)
      b2 = y3 - a2 * x3
        
      x = x1
      y = a2 * x + b2
        
    # 한 선분이 y축에 평행한 경우 (3)
    elif x1 != x2 and x3 == x4:
      a1 = (y2 - y1) / (x2 - x1)
      b1 = y1 - a1 * x1
        
      x = x3
      y = a1 * x + b1
        
    print(x, y)
        
  else:
    print(0)
  