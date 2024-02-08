import sys
input = lambda: sys.stdin.readline().rstrip()
INF = -1000001

def solve(N, M, land):
	# 왼쪽에서 오른쪽으로
	left = [[INF] * (M + 2) for _ in range(N + 2)]
	
	# 오른쪽에서 왼쪽으로
	right = [[INF] * (M + 2) for _ in range(N + 2)]
	
	# 최종 결과
	memo = [[INF] * (M + 2) for _ in range(N + 2)]
	
	# 왼쪽 위에서 시작
	left[0][1] = left[1][0] = 0
	
	for row in range(1, N + 1):
		for col in range(1, M + 1):
			left[row][col] = land[row - 1][col - 1] + max(memo[row - 1][col], left[row][col - 1])
		
		for col in range(M, 0, -1):
			right[row][col] = land[row - 1][col - 1] + max(memo[row - 1][col], right[row][col + 1])
		
		for col in range(1, M + 1):
			memo[row][col] = max(left[row][col], right[row][col])
	
	return memo[N][M]

if __name__ == "__main__":
	N, M = map(int, input().split())
	land = [[*map(int, input().split())] for _ in range(N)]
	
	print(solve(N, M, land))
	