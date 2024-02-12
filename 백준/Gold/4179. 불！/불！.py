import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e10)
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
PLAYER, FIRE = 0, 1

def solve(N, M, data):
	result = INF
	
	memo = [[INF] * M for _ in range(N)]
	queue = deque([])
	
	# 플레이어의 초기 위치
	player = None
	
	for row in range(N):
		for col in range(M):
			if data[row][col] == 'J':
				player = (row, col)
				memo[row][col] = 0
			
			if data[row][col] == 'F':
				queue.append((FIRE, row, col))
				memo[row][col] = 0
	
	# 지훈의 위치를 가장 마지막에 탐색하도록 한다!
	queue.append((PLAYER, *player))
	
	while queue:
		type, row, col = queue.popleft()
		
		for x in range(4):
			nrow, ncol = row + dr[x], col + dc[x]
			
			if not (0 <= nrow < N and 0 <= ncol < M):
				# 미로를 탈출하는 경우
				if type == PLAYER:
					result = min(result, memo[row][col] + 1)
					
				continue
				
			# 벽에 부딪히는 경우
			if data[nrow][ncol] == '#':
				continue
			
			if memo[nrow][ncol] <= memo[row][col] + 1:
				continue
			
			memo[nrow][ncol] = memo[row][col] + 1
			queue.append((type, nrow, ncol))
	
	return result if result < INF else "IMPOSSIBLE"

if __name__ == "__main__":
	N, M = map(int, input().split())
	data = [[*input()] for _ in range(N)]
	
	print(solve(N, M, data))
