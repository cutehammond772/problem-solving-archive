import sys
input = lambda: sys.stdin.readline().rstrip()
UNDEFINED, COVERED, DIVIDED = -1, 0, 1

def backtrack(x, y, k, track, plug, connections):
	result, info = track[x][y][k]

	if result == COVERED:
		plug.append(x)
		connections[x], connections[y] = y, x

		backtrack(x + 1, y - 1, k - 1, track, plug, connections)
	elif result == DIVIDED:
		t, w = info

		backtrack(x, t, w, track, plug, connections)
		backtrack(t + 1, y, k - w, track, plug, connections)

def solve(N, K, U):
	# Case 1. dp[1][N][K] = (U[1] * U[N]) + dp[2][N - 1][K - 1]
	# Case 2. dp[1][N][K] = max(dp[1][x][w] + dp[x + 1][N][K - w])

	# dp[x][y][k] => [x, y] 구간에서 k개의 전선을 연결할 때의 최대 누적 중요도 값
	dp = [[[0 for _ in range(K + 1)] for _ in range(N + 1)] for _ in range(N + 1)]

	# track[x][y][k] = [UNDEFINED|COVERED|DIVIDED, None|None|(p, w)]
	track = [[[[UNDEFINED, None] for _ in range(K + 1)] for _ in range(N + 1)] for _ in range(N + 1)]

	for l in range(1, N + 1):
		for o in range(1, N + 1):
			x, y = o, o + (l - 1)
			if y > N: break

			for k in range(1, min(l, K) + 1):
				# Case 1. 가장자리를 회로로 감싸기
				priority = U[x] * U[y] if x != y else U[x]

				if k == 1:
					if dp[x][y][k] < priority:
						dp[x][y][k] = priority
						track[x][y][k] = [COVERED, None]

				elif y - x >= 2:
					inner = dp[x + 1][y - 1][k - 1]

					if inner:
						if dp[x][y][k] < priority + inner:
							dp[x][y][k] = priority + inner
							track[x][y][k] = [COVERED, None]

				# Case 2. 두 구간으로 분할하여 생각해보기
				for t in range(x, y):
					if dp[x][y][k] < dp[x][t][k]:
						dp[x][y][k] = dp[x][t][k]
						track[x][y][k] = [DIVIDED, (t, k)]

					if dp[x][y][k] < dp[t + 1][y][k]:
						dp[x][y][k] = dp[t + 1][y][k]
						track[x][y][k] = [DIVIDED, (t, 0)]

					for w in range(1, k):
						left, right = dp[x][t][w], dp[t + 1][y][k - w]

						if left and right:
							if dp[x][y][k] < dp[x][t][w] + dp[t + 1][y][k - w]:
								dp[x][y][k] = dp[x][t][w] + dp[t + 1][y][k - w]
								track[x][y][k] = [DIVIDED, (t, w)]

	plug, connections = [], [0] * (N + 1)
	MAX_K = max(range(1, K + 1), key=lambda k: dp[1][N][k])
	backtrack(1, N, MAX_K, track, plug, connections)
	plug.sort()

	return ([0] * (K - MAX_K)) + plug, connections[1:]

if __name__ == '__main__':
	N, K = map(int, input().split())
	U = [0] + [*map(int, input().split())]

	plug, connections = solve(N, K, U)
	print(*plug, sep='\n')
	print(*connections, sep='\n')
