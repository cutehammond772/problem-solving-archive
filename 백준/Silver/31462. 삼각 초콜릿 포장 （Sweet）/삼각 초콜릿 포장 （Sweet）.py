import sys
input = lambda: sys.stdin.readline().rstrip()

RED = [(0, 0), (1, 0), (1, 1)]
BLUE = [(0, 0), (0, 1), (1, 1)]

def solve(N, A):
	check = [[False] * (1 + x) for x in range(N)]
	
	for row in range(N):
		for col in range(1 + row):
			if check[row][col]:
				continue
			
			# 처음 직면한 색깔이 빨간색인 경우
			if A[row][col] == "R":
				for p, q in RED:
					nrow, ncol = row + p, col + q
					
					if not (0 <= nrow < N and 0 <= ncol < 1 + nrow):
						return 0
					
					if A[nrow][ncol] != "R":
						return 0
					
					if check[nrow][ncol]:
						return 0
					
					check[nrow][ncol] = True
					
			# 처음 직면한 색깔이 파란색인 경우
			if A[row][col] == "B":
				for p, q in BLUE:
					nrow, ncol = row + p, col + q
					
					if not (0 <= nrow < N and 0 <= ncol < 1 + nrow):
						return 0
						
					if A[nrow][ncol] != "B":
						return 0
					
					if check[nrow][ncol]:
						return 0
						
					check[nrow][ncol] = True
	
	return 1

if __name__ == '__main__':
	N = int(input())
	A = [[*input()] for _ in range(N)]
	
	print(solve(N, A))
		