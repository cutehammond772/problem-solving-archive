import sys
from heapq import heappush, heappop
input = lambda: sys.stdin.readline().rstrip()

I, D = 0, 1
convert = { 'I': I, 'D': D }

def pop(check, heap):
  while heap:
    _, _, id = heap[0]
    
    if check[id]:
      heappop(heap)
      continue

    _, num, check_id = heappop(heap)
    check[check_id] = True
    
    return num, False
    
  return -1, True

def solve(commands):
  # 각 원소에 고유의 ID를 부여한다.
  check = [False] * 1000000
  check_id = 0

  # 최소힙과 최대힙을 나타낸다.
  maxheap, minheap = [], []
  
  for cmd, num in commands:
    if cmd == I:
      heappush(minheap, (num, num, check_id))
      heappush(maxheap, (-num, num, check_id))

      check_id += 1
      
    elif cmd == D:
      if num == 1:
        pop(check, maxheap)
      elif num == -1:
        pop(check, minheap)

  max_result, max_empty = pop(check, maxheap)
  min_result, min_empty = pop(check, minheap)

  if max_empty:
    return "EMPTY"

  if min_empty:
    return f"{max_result} {max_result}"

  return f"{max_result} {min_result}"
  
if __name__ == '__main__':
  T = int(input())
  
  for _ in range(T):
    N = int(input())
    commands = []
    
    for _ in range(N):
      cmd, num = input().split()
      commands.append((convert[cmd], int(num)))
      
    print(solve(commands))