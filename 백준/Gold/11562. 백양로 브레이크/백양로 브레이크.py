import sys
input = lambda: sys.stdin.readline().rstrip()
INF = int(1e10)

if __name__ == "__main__":
	N, M = map(int, input().split())
	memo = [[INF] * (N + 1) for _ in range(N + 1)]

	# 1. 길 구성하기
	for _ in range(M):
		u, v, b = map(int, input().split())

		# 양방향 길인 경우
		if b == 1:
			memo[u][v] = memo[v][u] = 0

		# 일방통행인 경우
		if b == 0:
			memo[u][v] = 0
			memo[v][u] = 1

	# 2. Floyd-Warshall을 이용하여 최소 구하기
	for i in range(1, N + 1):
		memo[i][i] = 0

	for k in range(1, N + 1):
		for i in range(1, N + 1):
			for j in range(1, N + 1):
				memo[i][j] = min(memo[i][j], memo[i][k] + memo[k][j])

	# 3. 쿼리를 받아 처리하기
	K = int(input())

	for _ in range(K):
		s, e = map(int, input().split())
		print(memo[s][e])
