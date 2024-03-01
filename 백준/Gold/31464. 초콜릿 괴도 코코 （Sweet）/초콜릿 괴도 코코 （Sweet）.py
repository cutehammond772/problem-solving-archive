import sys
input = lambda: sys.stdin.readline().rstrip()
dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]

def check(N, data):
	area = 0
	discover = [[-1] * N for _ in range(N)]
	
	for i in range(N):
		for j in range(N):
			if data[i][j] == '.':
				continue
			
			if discover[i][j] >= 0:
				continue
			
			stack = [(-1, -1, i, j)]
			discover[i][j] = area
			
			while stack:
				prow, pcol, row, col = stack.pop()
				
				for x in range(4):
					nrow, ncol = row + dr[x], col + dc[x]
					
					if (nrow, ncol) == (prow, pcol):
						continue
					
					if not (0 <= nrow < N and 0 <= ncol < N):
						continue
					
					if data[nrow][ncol] == '.':
						continue
					
					# 사이클이 존재하는 경우
					if discover[nrow][ncol] >= 0:
						return False
					
					discover[nrow][ncol] = area
					stack.append((row, col, nrow, ncol))
			
			area += 1
	
	# 구역이 처음부터 둘로 나뉘어져 있으면 안 된다.
	return area == 1

def solve(N, data):
	result = []
	
	# 특정 초콜릿을 제거한 경우
	for row in range(N):
		for col in range(N):
			if data[row][col] == '.':
				continue
			
			data[row][col] = '.'
			
			if check(N, data):
				result.append((row, col))
			
			data[row][col] = '#'
	
	return result

if __name__ == '__main__':
	N = int(input())
	data = [[*input()] for _ in range(N)]
	
	result = solve(N, data)
	print(len(result))
	
	for row, col in result:
		print(row + 1, col + 1)
	