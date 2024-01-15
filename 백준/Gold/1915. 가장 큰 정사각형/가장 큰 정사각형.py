import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, matrix):
	result = 0
	
	for row in range(N):
		for col in range(M):
			if matrix[row][col] == 0:
				continue
			
			if row > 0 and col > 0:
				matrix[row][col] = min(
					matrix[row - 1][col],
					matrix[row][col - 1],
					matrix[row - 1][col - 1]
				) + 1
			
			result = max(result, matrix[row][col])
			
	return result ** 2

if __name__ == '__main__':
	N, M = map(int, input().split())
	matrix = [[int(ch) for ch in input()] for _ in range(N)]
	
	print(solve(N, M, matrix))
	