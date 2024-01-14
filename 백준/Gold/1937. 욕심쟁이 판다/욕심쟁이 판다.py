import sys
sys.setrecursionlimit(10 ** 5)
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def solve(N, matrix):
	memo = [[0] * N for _ in range(N)]
	result = 0
	
	def traverse(row, col):
		nonlocal result
		
		if memo[row][col]:
			return memo[row][col]
		
		move = 0
		
		for i in range(4):
			nrow, ncol = row + dr[i], col + dc[i]
			
			if not (0 <= nrow < N and 0 <= ncol < N):
				continue
			
			if matrix[row][col] >= matrix[nrow][ncol]:
				continue
			
			move = max(move, traverse(nrow, ncol))
		
		memo[row][col] = 1 + move
		result = max(result, memo[row][col])
		
		return memo[row][col]
	
	for row in range(N):
		for col in range(N):
			traverse(row, col)
	
	return result

if __name__ == '__main__':
	N = int(input())
	matrix = [[*map(int, input().split())] for _ in range(N)]
	
	print(solve(N, matrix))
	