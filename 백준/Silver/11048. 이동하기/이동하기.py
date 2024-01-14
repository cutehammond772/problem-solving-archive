import sys
input = lambda: sys.stdin.readline().rstrip()

if __name__ == '__main__':
	N, M = map(int, input().split())
	matrix = [[*map(int, input().split())] for _ in range(N)]
	
	for row in range(N):
		for col in range(M):
			candidate = [0]
			
			if col > 0:
				candidate.append(matrix[row][col - 1])
			
			if row > 0:
				candidate.append(matrix[row - 1][col])
			
			if row > 0 and col > 0:
				candidate.append(matrix[row - 1][col - 1])
			
			matrix[row][col] += max(candidate)
	
	print(matrix[-1][-1])
	