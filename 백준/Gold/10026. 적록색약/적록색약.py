import sys
from queue import Queue

input = lambda: sys.stdin.readline().strip()

NON_WEAK, WEAK = 0, 1

def solve(visit, area, N):
  area_non_weak, area_weak = 0, 0
  que = Queue()

  def mark(row_p, col_p, row_q, col_q, status):
    nonlocal que
    
    if area[row_p][col_p] != area[row_q][col_q]:
      if status == WEAK and (
        area[row_p][col_p] == 'R' and area[row_q][col_q] == 'G' or
        area[row_p][col_p] == 'G' and area[row_q][col_q] == 'R'
      ):
        visit[row_q][col_q][status] = True
        que.put((row_q, col_q, status))
    else:
      visit[row_q][col_q][status] = True
      que.put((row_q, col_q, status))
            
  for row_idx in range(N):
    for col_idx in range(N):
      if not visit[row_idx][col_idx][NON_WEAK]:
        que.put((row_idx, col_idx, NON_WEAK))
        visit[row_idx][col_idx][NON_WEAK] = True
        area_non_weak += 1
        
      if not visit[row_idx][col_idx][WEAK]:
        que.put((row_idx, col_idx, WEAK))
        visit[row_idx][col_idx][WEAK] = True
        area_weak += 1
      
      while not que.empty():
        row, col, status = que.get()
        
        # (0, +1)
        if col + 1 <= N - 1 and not visit[row][col + 1][status]:
          mark(row, col, row, col + 1, status)
          
        # (+1, 0)
        if row + 1 <= N - 1 and not visit[row + 1][col][status]:
          mark(row, col, row + 1, col, status)
          
        # (0, -1)
        if col > 0 and not visit[row][col - 1][status]:
          mark(row, col, row, col - 1, status)
          
        # (-1, 0)
        if row > 0 and not visit[row - 1][col][status]:
          mark(row, col, row - 1, col, status)
          
  return area_non_weak, area_weak

if __name__ == '__main__':
  N = int(input())
  area = [input() for _ in range(N)]
  visit = [[[False, False] for _ in range(N)] for _ in range(N)]
  
  area_non_weak, area_weak = solve(visit, area, N)
  print(area_non_weak, area_weak)