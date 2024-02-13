import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def check(N, K, area):
	count = 0
	
	queue = deque([])
	discover = [[False] * N for _ in range(N)]
	
	for row in range(N):
		for col in range(N):
			if discover[row][col] or area[row][col] <= K:
				continue
			
			count += 1
			
			discover[row][col] = True
			queue.append((row, col))
			
			while queue:
				curr_row, curr_col = queue.popleft()
				
				for x in range(4):
					next_row, next_col = curr_row + dr[x], curr_col + dc[x]
					
					if not (0 <= next_row < N and 0 <= next_col < N):
						continue
					
					if discover[next_row][next_col] or area[next_row][next_col] <= K:
						continue
					
					discover[next_row][next_col] = True
					queue.append((next_row, next_col))
	
	return count

def solve(N, area):
	return max(check(N, k, area) for k in range(101))

if __name__ == "__main__":
	N = int(input())
	area = [[*map(int, input().split())] for _ in range(N)]
	
	print(solve(N, area))
	