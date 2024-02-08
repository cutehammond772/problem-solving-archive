import sys
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def solve(N, M, board):
	memo = [[0] * M for _ in range(N)]
	visit = [[False] * M for _ in range(N)]
	
	# 무한대 체크
	infinite = False
	
	def find(row, col):
		nonlocal infinite
		result = 0
		
		if infinite:
			return -1
		
		if memo[row][col]:
			return memo[row][col]
		
		# 현재 위치의 방문 체크
		visit[row][col] = True
		
		for x in range(4):
			nrow, ncol = row + (dr[x] * board[row][col]), col + (dc[x] * board[row][col])
			
			if not (0 <= nrow < N and 0 <= ncol < M):
				continue
			
			if not board[nrow][ncol]:
				continue
			
			if visit[nrow][ncol]:
				infinite = True
				return -1
			
			result = max(result, find(nrow, ncol))
		
		memo[row][col] = 1 + result
		visit[row][col] = False
		
		return memo[row][col]
	
	result = find(0, 0)
	return result if not infinite else -1

if __name__ == "__main__":
	N, M = map(int, input().split())
	board = [[int(ch) for ch in input().replace('H', '0')] for _ in range(N)]
	
	print(solve(N, M, board))
	