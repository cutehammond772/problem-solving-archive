import sys
input = lambda: sys.stdin.readline().rstrip()

def ccw(x1, y1, x2, y2, x3, y3):
  result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)
  return 1 if result > 0 else -1 if result < 0 else 0

def compare(x1, y1, x2, y2):
  if x1 == x2:
    return y2 - y1
    
  return x2 - x1

if __name__ == '__main__':
  x1, y1, x2, y2 = map(int, input().split())
  x3, y3, x4, y4 = map(int, input().split())

  # 교차 여부 확인
  L1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
  L2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
  
  # 세 점 이상이 한 선 위에 있을 때 접하는 여부 확인
  if L1 == 0 and L2 == 0:
    if compare(x1, y1, x2, y2) < 0:
      x1, x2 = x2, x1
      y1, y2 = y2, y1
      
    if compare(x3, y3, x4, y4) < 0:
      x3, x4 = x4, x3
      y3, y4 = y4, y3

    print(1 if compare(x1, y1, x4, y4) >= 0 and compare(x3, y3, x2, y2) >= 0 else 0)
  else:
    print(1 if L1 <= 0 and L2 <= 0 else 0)