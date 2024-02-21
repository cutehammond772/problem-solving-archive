import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [-1, -1, -1, 0, 1, 1, 1, 0], [-1, 0, 1, 1, 1, 0, -1, -1]

def solve(N, M, matrix):
	discover = [[False] * M for _ in range(N)]
	queue = deque([])
	count = 0
	
	for i in range(N):
		for j in range(M):
			# 이미 체크한 경우
			if discover[i][j]:
				continue
			
			# 바다인 경우
			if matrix[i][j] == 0:
				continue
			
			discover[i][j] = True
			queue.append((i, j))
			count += 1
			
			while queue:
				row, col = queue.popleft()
				
				for x in range(8):
					nrow, ncol = row + dr[x], col + dc[x]
					
					if not (0 <= nrow < N and 0 <= ncol < M):
						continue
					
					if matrix[nrow][ncol] == 0:
						continue
					
					if discover[nrow][ncol]:
						continue
					
					discover[nrow][ncol] = True
					queue.append((nrow, ncol))
	
	return count
	
if __name__ == "__main__":
	while (data := input()) != "0 0":
		M, N = map(int, data.split())
		matrix = [[*map(int, input().split())] for _ in range(N)]
		
		print(solve(N, M, matrix))
		