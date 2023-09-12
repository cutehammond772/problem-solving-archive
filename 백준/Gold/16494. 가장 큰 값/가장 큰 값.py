import sys
input = lambda: sys.stdin.readline().rstrip()
INF = -2001

def solve(N, M, Q):
	# memo[x][y]: x번째 원소를 포함하는 그룹 중 그룹이 y개인 것
	memo = [[INF] * 21 for _ in range(21)]
	memo[0][1] = 0

	for x in range(1, N + 1):
		memo[x][1] = max(memo[x - 1][1] + Q[x - 1], Q[x - 1])

		for y in range(2, x + 1):
			memo[x][y] = memo[x - 1][y] + Q[x - 1]

			for z in range(y - 1, x):
				memo[x][y] = max(memo[x][y], memo[z][y - 1] + Q[x - 1])

	return max(memo[x][M] for x in range(1, N + 1))

if __name__ == "__main__":
	N, M = map(int, input().split())
	Q = [*map(int, input().split())]
	print(solve(N, M, Q))
