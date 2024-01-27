import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

# 초기 상어의 위치를 구한다.
def find_shark(N, area):
	for row in range(N):
		for col in range(N):
			if area[row][col] == 9:
				return row, col
	
	return -1, -1

# 먹이를 찾는다.
def find_food(N, area, shark_row, shark_col, size):
	visited = [[False] * N for _ in range(N)]
	queue = deque([])
	candidate = []
	
	queue.append((0, shark_row, shark_col))
	visited[shark_row][shark_col] = True
	
	while queue:
		dist, row, col = queue.popleft()
		
		for x in range(4):
			nrow, ncol = row + dr[x], col + dc[x]
			
			if not (0 <= nrow < N and 0 <= ncol < N):
				continue
			
			if visited[nrow][ncol]:
				continue
			
			# 자신보다 크기가 큰 물고기가 있는 칸은 지나갈 수 없다.
			if area[nrow][ncol] > size:
				continue
			
			visited[nrow][ncol] = True
			
			if area[nrow][ncol] == size or area[nrow][ncol] == 0:
				queue.append((dist + 1, nrow, ncol))
			
			# 먹이를 찾았을 경우, 더 이동할 필요가 없다.
			else:
				candidate.append((dist + 1, nrow, ncol))
	
	if not candidate:
		return None
	
	return min(candidate)

def solve(N, area):
	shark_row, shark_col = find_shark(N, area)
	
	# 상어의 크기
	size = 2
	
	# 먹은 물고기 수 (size만큼 먹으면 0으로 초기화)
	streak = 0
	
	# 경과된 시간
	time = 0
	
	# 아기 상어가 있는 칸을 빈 공간으로 간주한다. (별도로 관리)
	area[shark_row][shark_col] = 0
	
	while data := find_food(N, area, shark_row, shark_col, size):
		elapsed_time, shark_row, shark_col = data
		
		# 먹이를 섭취하였으므로 빈 공간으로 바꾼다.
		area[shark_row][shark_col] = 0
		streak += 1
		time += elapsed_time
		
		if streak == size:
			size += 1
			streak = 0
	
	return time

if __name__ == "__main__":
	N = int(input())
	area = [[*map(int, input().split())] for _ in range(N)]
	
	print(solve(N, area))
	