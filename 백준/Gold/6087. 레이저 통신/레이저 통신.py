import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e4 + 1)
V, H = 0, 1
dr, dc = [-1, 1, 0, 0], [0, 0, -1, 1]

def find(N, M, data):
	points = []
	
	for row in range(N):
		for col in range(M):
			if data[row][col] == 'C':
				points.append((row, col))
	
	return points

def solve(N, M, data):
	memo = [[[INF] * M for _ in range(N)] for _ in range(2)]
	queue = deque([])
	
	# 두 지점을 찾는다.
	start, dest = find(N, M, data)
	
	queue.append((V, *start))
	queue.append((H, *start))
	memo[V][start[0]][start[1]] = memo[H][start[0]][start[1]] = 0
	
	while queue:
		dir, row, col = queue.popleft()
		
		for x in range(4):
			nrow, ncol = row + dr[x], col + dc[x]
			
			# 바운더리 체크
			if not (0 <= nrow < N and 0 <= ncol < M):
				continue
			
			if data[nrow][ncol] == '*':
				continue
			
			ndir = x >> 1
			cost = dir != ndir
			
			if memo[ndir][nrow][ncol] <= memo[dir][row][col] + cost:
				continue
			
			memo[ndir][nrow][ncol] = memo[dir][row][col] + cost
			queue.append((ndir, nrow, ncol))
	
	return min(memo[V][dest[0]][dest[1]], memo[H][dest[0]][dest[1]])

if __name__ == "__main__":
	M, N = map(int, input().split())
	data = [[*input()] for _ in range(N)]
	
	print(solve(N, M, data))
