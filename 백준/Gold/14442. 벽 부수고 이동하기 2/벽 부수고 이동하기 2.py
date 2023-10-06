import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

dr, dc = [0, 1, 0, -1], [1, 0, -1, 0]
INF = 1000001

def solve(N, M, K, walls):
	memo = [[[INF] * (K + 1) for _ in range(M)] for _ in range(N)]
	queue = deque([])

	# 시작 지점에 대한 초기 설정
	queue.append((0, 0, 0, 1))

	for x in range(K + 1):
		memo[0][0][x] = 1

	while queue:
		row, col, wall, dist = queue.popleft()

		if (row, col) == (N - 1, M - 1):
			continue

		if memo[N - 1][M - 1][wall] <= dist:
			continue

		for x in range(4):
			nrow, ncol, nwall = row + dr[x], col + dc[x], wall

			if not (0 <= nrow < N and 0 <= ncol < M):
				continue

			if walls[nrow][ncol]:
				if nwall + 1 > K:
					continue

				nwall += 1

			if memo[nrow][ncol][nwall] <= dist + 1:
				continue

			for w in range(nwall, K + 1):
				memo[nrow][ncol][w] = min(memo[nrow][ncol][w], dist + 1)

			queue.append((nrow, ncol, nwall, dist + 1))

	result = memo[N - 1][M - 1][K]
	return result if result < INF else -1

if __name__ == "__main__":
	N, M, K = map(int, input().split())
	matrix = [[int(x) for x in input()] for _ in range(N)]

	print(solve(N, M, K, matrix))
