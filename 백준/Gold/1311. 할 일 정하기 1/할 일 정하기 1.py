import sys
input = lambda: sys.stdin.readline().rstrip()
INF = 200001

# (N명의 사람)과 (N개의 일)을 어떻게 매칭할까?
def solve(N, matrix):
	memo = [[INF] * (1 << N) for _ in range(N)]

	for w in range(N):
		memo[0][1 << w] = matrix[0][w]

	for x in range(1, N):
		for m in range(1 << N):
			if memo[x - 1][m] == INF:
				continue

			for w in range(N):
				if m & (1 << w):
					continue

				memo[x][m | (1 << w)] = min(memo[x][m | (1 << w)], memo[x - 1][m] + matrix[x][w])

	return memo[N - 1][(1 << N) - 1]

if __name__ == "__main__":
	N = int(input())
	matrix = [[*map(int, input().split())] for _ in range(N)]

	print(solve(N, matrix))
