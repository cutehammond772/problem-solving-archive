import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

INF = 11
BLANK, WALL = 0, 1
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def analyse(N, M, data):
	result = [[BLANK] * M for _ in range(N)]
	players = []
	
	for row in range(N):
		for col in range(M):
			if data[row][col] == '#':
				result[row][col] = WALL
			
			if data[row][col] == 'o':
				players.append(row * M + col)
	
	return result, players

def solve(N, M, data, p1, p2):
	result = INF
	memo = [[INF] * 400 for _ in range(400)]
	
	queue = deque([(p1, p2)])
	memo[p1][p2] = 0
	
	def out_of_bound(row, col):
		return not (0 <= row < N and 0 <= col < M)
	
	while queue:
		p1, p2 = queue.popleft()
		
		# 두 동전에 대해..
		for x in range(4):
			rp1, cp1 = (p1 // M) + dr[x], (p1 % M) + dc[x]
			rp2, cp2 = (p2 // M) + dr[x], (p2 % M) + dc[x]
			
			# 벽에 부딪힌 경우 이동하지 않는다.
			if not out_of_bound(rp1, cp1) and data[rp1][cp1] == WALL:
				rp1, cp1 = p1 // M, p1 % M
			
			if not out_of_bound(rp2, cp2) and data[rp2][cp2] == WALL:
				rp2, cp2 = p2 // M, p2 % M
			
			# 두 동전이 모두 떨어지는 경우 고려하지 않는다.
			if out_of_bound(rp1, cp1) and out_of_bound(rp2, cp2):
				continue
			
			# 동전이 한 곳에 합쳐지는 경우 두 동전이 항상 동시에 떨어지게 된다.
			if (rp1, cp1) == (rp2, cp2):
				continue
			
			# 한 동전만 떨어지는 경우 결과에 기록한다.
			if out_of_bound(rp1, cp1) ^ out_of_bound(rp2, cp2):
				result = min(result, memo[p1][p2] + 1)
				continue
				
			# 다음 상태
			np1, np2 = rp1 * M + cp1, rp2 * M + cp2
			
			if memo[np1][np2] <= memo[p1][p2] + 1:
				continue
			
			memo[np1][np2] = memo[p1][p2] + 1
			queue.append((np1, np2))
	
	return result if result < INF else -1

if __name__ == "__main__":
	N, M = map(int, input().split())
	data, players = analyse(N, M, [[*input()] for _ in range(N)])
	
	print(solve(N, M, data, *players))
	