import sys
input = lambda: sys.stdin.readline().rstrip()

def solve(N, M, Q):
	memo = [[0] * (M + 1) for _ in range(N + 1)]

	for x in range(1, N + 1):
		memo[x][0] = 1

		for k in range(1, M + 1):
			if k >= Q[x]:
				memo[x][k] = memo[x - 1][k] + memo[x][k - Q[x]]
			else:
				memo[x][k] = memo[x - 1][k]

	return memo[N][M]

if __name__ == "__main__":
	T = int(input())

	for _ in range(T):
		N = int(input())
		Q = [0, *map(int, input().split())]
		M = int(input())

		print(solve(N, M, Q))
