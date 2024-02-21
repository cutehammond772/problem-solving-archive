import sys
input = lambda: sys.stdin.readline().rstrip()
	
if __name__ == "__main__":
	N, M = map(int, input().split())
	matrix = [[0] * (N + 1) for _ in range(N + 1)]
	
	for row in range(1, N + 1):
		matrix[row] = [0, *map(int, input().split())]
	
	# 1. 누적 합 전처리
	for row in range(1, N + 1):
		for col in range(1, N + 1):
			matrix[row][col] += matrix[row][col - 1]
		
		for col in range(1, N + 1):
			matrix[row][col] += matrix[row - 1][col]
	
	# 2. 쿼리 처리
	for _ in range(M):
		x1, y1, x2, y2 = map(int, input().split())
		print(matrix[x2][y2] - matrix[x1 - 1][y2] - matrix[x2][y1 - 1] + matrix[x1 - 1][y1 - 1])