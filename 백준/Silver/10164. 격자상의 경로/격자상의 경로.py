import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, K):
	memo = [[0] * M for _ in range(N)]
	
	# 출발점
	memo[0][0] = 1
	
	# K = 0인 경우 중간점을 도착점으로 지정한다.
	if K == 0:
		K = N * M
	
	P, Q = (K - 1) // M, (K - 1) % M
	
	# 출발점 ~ 중간점
	for row in range(P + 1):
		for col in range(Q + 1):
			if row > 0:
				memo[row][col] += memo[row - 1][col]
			
			if col > 0:
				memo[row][col] += memo[row][col - 1]
	
	# 중간점 ~ 도착점
	for row in range(P, N):
		for col in range(Q, M):
			if row > P:
				memo[row][col] += memo[row - 1][col]
			
			if col > Q:
				memo[row][col] += memo[row][col - 1]
	
	return memo[N - 1][M - 1]

if __name__ == '__main__':
	N, M, K = map(int, input().split())
	print(solve(N, M, K))
	