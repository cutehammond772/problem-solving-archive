import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M):
  result, offset = 0, 0
  idxes = [(M[x], x) for x in range(N)]
  bottom = min(M)
  
  stack = [(bottom, 0)]
  
  while True:
    if offset >= N:
      break
      
    last_height, last_idx = stack[-1]
    curr_height, curr_idx = idxes[offset]
    offset += 1

    supply_idx = -1
    
    while last_height > curr_height:
      rectangle = last_height * (curr_idx - last_idx)
      result = max(result, rectangle)
      
      stack.pop()
      supply_idx = last_idx
      last_height, last_idx = stack[-1]

    if supply_idx >= 0:
      stack.append((curr_height, supply_idx))
      
    stack.append((curr_height, curr_idx))

  while stack:
    last_height, last_idx = stack.pop()
    rectangle = last_height * (N - last_idx)
      
    result = max(result, rectangle)
  
  return result
    
if __name__ == '__main__':
  N = int(input())
  M = [int(input()) for x in range(N)]

  print(solve(N, M))