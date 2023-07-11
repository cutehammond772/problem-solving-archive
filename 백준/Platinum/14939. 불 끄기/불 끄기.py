import sys
input = lambda: sys.stdin.readline().rstrip()

NaN = 101

def toggle_at(switches, row, col):
  # CENTER
  switches[row] ^= 1 << col

  # LEFT
  if col > 0:
    switches[row] ^= 1 << (col - 1)
    
  # RIGHT
  if col < 9:
    switches[row] ^= 1 << (col + 1)
    
  # UP
  if row > 0:
    switches[row - 1] ^= 1 << col

  # DOWN
  if row < 9:
    switches[row + 1] ^= 1 << col

def toggle(switches, offset, x):
  for k in range(10):
    if x & 1 << k > 0:
      toggle_at(switches, offset, k)

def ones_count(x):
  result = 0
  
  for k in range(10):
    if x & 1 << k > 0:
      result += 1
      
  return result

# 미리 구성
counts = [ones_count(x) for x in range(2 ** 10)]
ones = sorted(range(1024), key = lambda x: counts[x])

def solve(switches):
  result = NaN

  def recursion(offset, count):
    nonlocal result, switches

    if offset >= 10:
      if switches[9] == 0:
        result = min(result, count)
        
      return
    
    for x in ones:
      if count + counts[x] > result:
        break
        
      toggle(switches, offset, x)
      
      if not (offset > 0 and switches[offset - 1] > 0):
        recursion(offset + 1, count + counts[x])
        
      toggle(switches, offset, x)

  # 재귀적으로 수행
  recursion(0, 0)
  
  return result

if __name__ == '__main__':
  switches = []
  
  for x in range(10):
    bin, row = 0, input()
    
    for idx in range(10):
      if row[idx] == 'O':
        bin += 1 << idx
        
    switches.append(bin)

  result = solve(switches)
  print(result if result < NaN else -1)
    