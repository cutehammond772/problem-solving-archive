import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e10)
BLANK, WALL = 0, 1
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def analyse(N, M, data):
	# 해당 칸에 "가장 빨리" 불이 닿는 시간
	fire_map = [[INF] * M for _ in range(N)]
	fire_queue = deque([])
	
	# 벽과 빈 공간의 정보가 담겨져 있는 맵
	default_map = [[BLANK] * M for _ in range(N)]
	
	# 지훈이의 초기 위치
	player = None
	
	for row in range(N):
		for col in range(M):
			if data[row][col] == '#':
				default_map[row][col] = WALL
			
			elif data[row][col] == 'J':
				player = (row, col)
			
			elif data[row][col] == 'F':
				fire_map[row][col] = 0
				fire_queue.append((row, col))
		
	while fire_queue:
		row, col = fire_queue.popleft()
		
		for x in range(4):
			nrow, ncol = row + dr[x], col + dc[x]
			
			if not (0 <= nrow < N and 0 <= ncol < M):
				continue
			
			if default_map[nrow][ncol] == WALL:
				continue
			
			if fire_map[nrow][ncol] <= fire_map[row][col] + 1:
				continue
			
			fire_map[nrow][ncol] = fire_map[row][col] + 1
			fire_queue.append((nrow, ncol))
	
	return fire_map, default_map, player

def solve(N, M, data):
	result = INF
	fire_map, default_map, player = analyse(N, M, data)
	
	player_map = [[INF] * M for _ in range(N)]
	player_queue = deque([])
	
	player_queue.append(player)
	player_map[player[0]][player[1]] = 0
	
	while player_queue:
		row, col = player_queue.popleft()
		
		for x in range(4):
			nrow, ncol = row + dr[x], col + dc[x]
			
			# 미로를 탈출하는 경우
			if not (0 <= nrow < N and 0 <= ncol < M):
				result = min(result, player_map[row][col] + 1)
				continue
			
			# 벽에 부딪히는 경우
			if default_map[nrow][ncol] == WALL:
				continue
			
			# 해당 칸에 지훈이보다 불이 먼저 닿은 경우
			if fire_map[nrow][ncol] <= player_map[row][col] + 1:
				continue
			
			if player_map[nrow][ncol] <= player_map[row][col] + 1:
				continue
			
			player_map[nrow][ncol] = player_map[row][col] + 1
			player_queue.append((nrow, ncol))
	
	return result if result < INF else "IMPOSSIBLE"

if __name__ == "__main__":
	N, M = map(int, input().split())
	data = [[*input()] for _ in range(N)]
	
	print(solve(N, M, data))
	