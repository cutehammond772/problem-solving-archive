import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def union(U, x, y):
	x, y = find(U, x), find(U, y)
	
	if U[x] <= U[y]:
		U[y] = U[x]
	
	else:
		U[x] = U[y]

def find(U, x):
	if U[x] == x:
		return U[x]
	
	nodes = [x]
	
	while U[nodes[-1]] != nodes[-1]:
		nodes.append(U[nodes[-1]])
	
	for node in nodes:
		U[node] = nodes[-1]
	
	return U[x]

def solve(R, C, data):
	visited = [[False] * C for _ in range(R)]
	area = [*range(R * C)]
	
	# 해당 백조가 살고 있는 공간의 ID
	swans = []
	
	# 녹게 될 얼음 (time, row, col)
	ice = deque([])
	
	# 초기 물 공간 (id, row, col)
	water = deque([])
	
	for row in range(R):
		for col in range(C):
			if visited[row][col]:
				continue
			
			if data[row][col] == 'X':
				continue
				
			# 현재 물 공간의 고유 ID
			id = row * C + col
			water.append((row, col))
			
			while water:
				curr_row, curr_col = water.popleft()
				
				if data[curr_row][curr_col] == 'L':
					data[curr_row][curr_col] = '.'
					swans.append(id)
				
				for x in range(4):
					next_row, next_col = curr_row + dr[x], curr_col + dc[x]
					
					if not (0 <= next_row < R and 0 <= next_col < C):
						continue
					
					if visited[next_row][next_col]:
						continue
					
					visited[next_row][next_col] = True
					
					# 1초가 지난 경우 녹을 얼음
					if data[next_row][next_col] == 'X':
						ice.append((1, next_row, next_col))
						continue
					
					area[next_row * C + next_col] = id
					water.append((next_row, next_col))
	
	# 현재 시간
	current_time = 1
	
	while ice:
		# n초에 녹는 얼음까지만 판단
		while ice and ice[0][0] == current_time:
			_, row, col = ice.popleft()
			
			# 얼음이 녹아 물이 됨
			data[row][col] = '.'
			
			for x in range(4):
				nrow, ncol = row + dr[x], col + dc[x]
				
				if not (0 <= nrow < R and 0 <= ncol < C):
					continue
				
				if data[nrow][ncol] == '.':
					union(area, area[row * C + col], area[nrow * C + ncol])
				
				if visited[nrow][ncol]:
					continue
					
				visited[nrow][ncol] = True
				ice.append((current_time + 1, nrow, ncol))
		
		isolated = True
		
		for i in range(1, len(swans)):
			isolated &= find(area, swans[i - 1]) != find(area, swans[i])
		
		if not isolated:
			return current_time
		
		current_time += 1
	
	return None
	
if __name__ == "__main__":
	R, C = map(int, input().split())
	data = [[*input()] for _ in range(R)]
	
	print(solve(R, C, data))
	